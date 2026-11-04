import asyncio
import unittest

import httpx

from busbar_admin import AuthenticatedClient, Client
from busbar_admin.api.default import delete_api_v1_admin_hooks_name, get_api_v1_admin_info
from busbar_admin.errors import UnexpectedStatus
from busbar_admin.models.rotated_key_view import RotatedKeyView
from busbar_admin.types import Response


class ClientRegressions(unittest.TestCase):
    def test_credentials_not_in_repr(self):
        client = AuthenticatedClient(
            base_url="https://example.test",
            token="private-token",
            headers={"x-key": "private-header"},
            cookies={"session": "private-cookie"},
        )
        for secret in ("private-token", "private-header", "private-cookie"):
            self.assertNotIn(secret, repr(client))
        key = RotatedKeyView.from_dict(
            {
                "allowed_pools": None,
                "created_at": 0,
                "enabled": True,
                "group": None,
                "id": "id",
                "labels": {},
                "name": "name",
                "state": "active",
                "secret": "private-key",
            }
        )
        self.assertNotIn("private-key", repr(key))
        self.assertEqual(key.to_dict()["secret"], "private-key")
        response = Response(200, b"private-body", {"x-key": "private-header"}, key)
        for secret in ("private-body", "private-header", "private-key"):
            self.assertNotIn(secret, repr(response))

    def test_builders_do_not_mutate_existing_transports(self):
        for cls in (Client, AuthenticatedClient):
            kwargs = {"token": "token"} if cls is AuthenticatedClient else {}
            client = cls(
                base_url="https://example.test",
                headers={"x-id": "old"},
                cookies={"session": "old"},
                timeout=httpx.Timeout(3),
                **kwargs,
            )
            sync = client.get_httpx_client()
            async_client = client.get_async_httpx_client()
            changed = (
                client.with_headers({"x-id": "new"}).with_cookies({"session": "new"}).with_timeout(httpx.Timeout(8))
            )
            for transport in (sync, async_client):
                self.assertEqual(transport.headers["x-id"], "old")
                self.assertEqual(transport.cookies["session"], "old")
                self.assertEqual(transport.timeout.read, 3)
            self.assertEqual(changed.get_httpx_client().headers["x-id"], "new")
            changed.get_httpx_client().close()
            sync.close()
            asyncio.run(async_client.aclose())

    def test_nonstandard_status_obeys_error_policy(self):
        response = httpx.Response(599, content=b"private-body")
        client = Client(base_url="https://example.test")
        self.assertEqual(get_api_v1_admin_info._build_response(client=client, response=response).status_code, 599)
        client.raise_on_unexpected_status = True
        with self.assertRaises(UnexpectedStatus) as raised:
            get_api_v1_admin_info._build_response(client=client, response=response)
        self.assertEqual(raised.exception.content, b"private-body")
        self.assertNotIn("private-body", str(raised.exception))

    def test_dot_path_segments_remain_resource_names(self):
        for name in (".", ".."):
            kwargs = delete_api_v1_admin_hooks_name._get_kwargs(name)
            request = httpx.Request(kwargs["method"], "https://example.test" + kwargs["url"])
            self.assertEqual(request.url.raw_path, b"/api/v1/admin/hooks/" + b"%2E" * len(name))

    def test_invalid_credentials_are_rejected_without_echo(self):
        for token in ("secret\nvalue", "secret\x00value", "secret\x7fvalue", "secret-trailing "):
            client = AuthenticatedClient(base_url="https://example.test", token=token)
            with self.assertRaises(ValueError) as raised:
                client.get_httpx_client()
            self.assertNotIn("secret", str(raised.exception))

    def test_custom_token_does_not_follow_cross_origin_redirect(self):
        seen = []

        def handle(request):
            seen.append(request)
            if request.url.host == "example.test":
                return httpx.Response(302, headers={"location": "https://other.test/"})
            return httpx.Response(200)

        client = AuthenticatedClient(
            base_url="https://example.test",
            token="private-token",
            prefix="",
            auth_header_name="x-admin-token",
            follow_redirects=True,
            httpx_args={"transport": httpx.MockTransport(handle)},
        )
        with client:
            client.get_httpx_client().get("/")
        self.assertEqual(seen[0].headers["x-admin-token"], "private-token")
        self.assertNotIn("x-admin-token", seen[1].headers)

    def test_async_redirect_guard_preserves_same_origin_and_user_hooks(self):
        seen = []
        hook_headers = []

        def handle(request):
            seen.append(request)
            if request.url.path == "/":
                return httpx.Response(302, headers={"location": "/next"})
            if request.url.path == "/next":
                return httpx.Response(302, headers={"location": "https://other.test/final"})
            return httpx.Response(200)

        async def observe(request):
            hook_headers.append(request.headers.get("x-admin-token"))

        hooks = {"request": [observe]}
        client = AuthenticatedClient(
            base_url="https://example.test",
            token="private-token",
            prefix="",
            auth_header_name="x-admin-token",
            follow_redirects=True,
            httpx_args={"transport": httpx.MockTransport(handle), "event_hooks": hooks},
        )

        async def run():
            async with client:
                await client.get_async_httpx_client().get("/")

        asyncio.run(run())
        self.assertEqual(hook_headers, ["private-token", "private-token", None])
        self.assertEqual(hooks, {"request": [observe]})
        self.assertNotIn("x-admin-token", seen[-1].headers)

    def test_auth_header_overrides_case_insensitive_existing_header(self):
        client = AuthenticatedClient(
            base_url="https://example.test", token="new-token", headers={"authorization": "old-token"}
        )
        with client:
            self.assertEqual(client.get_httpx_client().headers.get_list("authorization"), ["Bearer new-token"])

    def test_builders_reject_implicitly_discarding_manual_transports(self):
        client = Client(base_url="https://original.test")
        with httpx.Client(base_url="https://custom.test") as custom:
            client.set_httpx_client(custom)
            for build in (
                lambda: client.with_headers({"x-id": "new"}),
                lambda: client.with_cookies({"session": "new"}),
                lambda: client.with_timeout(httpx.Timeout(4)),
            ):
                with self.assertRaisesRegex(ValueError, "manually supplied"):
                    build()
            self.assertIs(client.get_httpx_client(), custom)

    def test_constructor_does_not_modify_caller_headers(self):
        headers = {"x-id": "original"}
        client = AuthenticatedClient(base_url="https://example.test", token="private-token", headers=headers)
        client.get_httpx_client().close()
        self.assertEqual(headers, {"x-id": "original"})


if __name__ == "__main__":
    unittest.main()
