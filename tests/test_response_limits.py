import asyncio
import gzip
import unittest

import httpx

from busbar_admin import Client
from busbar_admin.api.default import get_api_v1_admin_openapi_json


class ResponseLimits(unittest.TestCase):
    def test_sync_size_limit_closes_response(self):
        class Body(httpx.SyncByteStream):
            closed = False

            def __iter__(self):
                yield b'{"body":"'
                yield b"x" * 64
                yield b'"}'

            def close(self):
                self.closed = True

        body = Body()
        client = Client(
            base_url="https://example.test",
            max_response_bytes=16,
            httpx_args={"transport": httpx.MockTransport(lambda request: httpx.Response(200, stream=body))},
        )
        with client:
            with self.assertRaisesRegex(ValueError, "response.*limit"):
                get_api_v1_admin_openapi_json.sync_detailed(client=client)
        self.assertTrue(body.closed)

    def test_async_size_limit_closes_response(self):
        class Body(httpx.AsyncByteStream):
            closed = False

            async def __aiter__(self):
                yield b"x" * 64

            async def aclose(self):
                self.closed = True

        body = Body()
        client = Client(
            base_url="https://example.test",
            max_response_bytes=16,
            httpx_args={"transport": httpx.MockTransport(lambda request: httpx.Response(200, stream=body))},
        )

        async def run():
            async with client:
                with self.assertRaisesRegex(ValueError, "response.*limit"):
                    await get_api_v1_admin_openapi_json.asyncio_detailed(client=client)

        asyncio.run(run())
        self.assertTrue(body.closed)

    def test_compressed_response_is_decoded_once_and_headers_preserved(self):
        data = b'{"example":"ok"}'
        client = Client(
            base_url="https://example.test",
            max_response_bytes=len(data),
            httpx_args={
                "transport": httpx.MockTransport(
                    lambda request: httpx.Response(
                        200, headers={"content-encoding": "gzip"}, stream=httpx.ByteStream(gzip.compress(data))
                    )
                )
            },
        )
        with client:
            response = get_api_v1_admin_openapi_json.sync_detailed(client=client)
        self.assertEqual(response.content, data)
        self.assertEqual(response.headers["content-encoding"], "gzip")
        self.assertEqual(response.parsed["example"], "ok")

    def test_redirect_bodies_share_sdk_budget_for_both_transports(self):
        for manual in (False, True):
            for asynchronous in (False, True):
                with self.subTest(manual=manual, asynchronous=asynchronous):
                    seen = []

                    def handle(request):
                        seen.append(request.url.path)
                        if request.url.path == "/api/v1/admin/openapi.json":
                            return httpx.Response(302, headers={"location": "/final"}, content=b"x" * 15)
                        return httpx.Response(200, json={})

                    transport = httpx.MockTransport(handle)
                    client = Client(
                        base_url="https://example.test",
                        max_response_bytes=16,
                        follow_redirects=True,
                        httpx_args={"transport": transport},
                    )
                    if asynchronous:
                        if manual:
                            client.set_async_httpx_client(
                                httpx.AsyncClient(
                                    base_url="https://example.test", follow_redirects=True, transport=transport
                                )
                            )

                        async def run():
                            async with client:
                                with self.assertRaisesRegex(ValueError, "response.*limit"):
                                    await get_api_v1_admin_openapi_json.asyncio_detailed(client=client)

                        asyncio.run(run())
                    else:
                        if manual:
                            client.set_httpx_client(
                                httpx.Client(
                                    base_url="https://example.test", follow_redirects=True, transport=transport
                                )
                            )
                        with client:
                            with self.assertRaisesRegex(ValueError, "response.*limit"):
                                get_api_v1_admin_openapi_json.sync_detailed(client=client)
                    self.assertEqual(seen, ["/api/v1/admin/openapi.json", "/final"])

    def test_manual_client_budget_is_per_sdk_request(self):
        transport = httpx.MockTransport(lambda request: httpx.Response(200, json={"padding": "x" * 20}))
        with httpx.Client(base_url="https://example.test", transport=transport) as underlying:
            small = Client(base_url="https://example.test", max_response_bytes=16).set_httpx_client(underlying)
            large = Client(base_url="https://example.test", max_response_bytes=64).set_httpx_client(underlying)
            self.assertEqual(len(underlying.event_hooks["response"]), 1)
            with self.assertRaisesRegex(ValueError, "response.*limit"):
                get_api_v1_admin_openapi_json.sync_detailed(client=small)
            self.assertEqual(get_api_v1_admin_openapi_json.sync_detailed(client=large).status_code, 200)
            self.assertEqual(underlying.get("/").status_code, 200)

    def test_auth_replacement_requests_keep_budget_and_decode_final_body(self):
        class ReplaceRequest(httpx.Auth):
            def auth_flow(self, request):
                response = yield request
                if response.status_code == 401:
                    response = yield httpx.Request("GET", request.url)
                    if response.status_code == 401:
                        yield request

        for oversized in (False, True):
            for asynchronous in (False, True):
                with self.subTest(oversized=oversized, asynchronous=asynchronous):
                    calls = []

                    def handle(request):
                        calls.append(request)
                        if len(calls) == 1:
                            return httpx.Response(401, content=b"")
                        if oversized and len(calls) == 2:
                            return httpx.Response(401, stream=httpx.ByteStream(b"x" * 102400))
                        return httpx.Response(200, stream=httpx.ByteStream(b"{}"))

                    client = Client(
                        base_url="https://example.test",
                        max_response_bytes=16,
                        httpx_args={"transport": httpx.MockTransport(handle), "auth": ReplaceRequest()},
                    )
                    if asynchronous:

                        async def run():
                            async with client:
                                if oversized:
                                    with self.assertRaisesRegex(ValueError, "response.*limit"):
                                        await get_api_v1_admin_openapi_json.asyncio_detailed(client=client)
                                else:
                                    result = await get_api_v1_admin_openapi_json.asyncio_detailed(client=client)
                                    self.assertEqual(result.status_code, 200)
                                    self.assertEqual(result.content, b"{}")

                        asyncio.run(run())
                    else:
                        with client:
                            if oversized:
                                with self.assertRaisesRegex(ValueError, "response.*limit"):
                                    get_api_v1_admin_openapi_json.sync_detailed(client=client)
                            else:
                                result = get_api_v1_admin_openapi_json.sync_detailed(client=client)
                                self.assertEqual(result.status_code, 200)
                                self.assertEqual(result.content, b"{}")
                    self.assertEqual(len(calls), 2)

    def test_concurrent_sdk_budgets_are_isolated_on_shared_async_client(self):
        async def handle(request):
            await asyncio.sleep(0)
            return httpx.Response(200, json={"padding": "x" * 20})

        async def run():
            async with httpx.AsyncClient(
                base_url="https://example.test", transport=httpx.MockTransport(handle)
            ) as underlying:
                small = Client(base_url="https://example.test", max_response_bytes=16).set_async_httpx_client(
                    underlying
                )
                large = Client(base_url="https://example.test", max_response_bytes=64).set_async_httpx_client(
                    underlying
                )

                async def call(client):
                    try:
                        return (await get_api_v1_admin_openapi_json.asyncio_detailed(client=client)).status_code
                    except ValueError:
                        return "limited"

                self.assertEqual(await asyncio.gather(call(small), call(large)), ["limited", 200])
                self.assertEqual((await underlying.get("/")).status_code, 200)

        asyncio.run(run())

    def test_completed_sdk_budget_does_not_limit_later_callback_task(self):
        async def run():
            released = asyncio.Event()
            pending = []

            async def response_hook(response):
                if response.request.url.path == "/api/v1/admin/openapi.json":

                    async def later():
                        await released.wait()
                        return await underlying.get("/background")

                    pending.append(asyncio.create_task(later()))

            def handle(request):
                return httpx.Response(200, content=b"{}" if request.url.path != "/background" else b"x" * 64)

            async with httpx.AsyncClient(
                base_url="https://example.test",
                transport=httpx.MockTransport(handle),
                event_hooks={"response": [response_hook]},
            ) as underlying:
                client = Client(base_url="https://example.test", max_response_bytes=16).set_async_httpx_client(
                    underlying
                )
                self.assertEqual((await get_api_v1_admin_openapi_json.asyncio_detailed(client=client)).status_code, 200)
                released.set()
                self.assertEqual((await pending[0]).status_code, 200)

        asyncio.run(run())

    def test_unrelated_hook_requests_do_not_inherit_sdk_budget(self):
        for asynchronous in (False, True):
            with self.subTest(asynchronous=asynchronous):

                def handle(request):
                    return httpx.Response(200, content=b"x" * 64 if request.url.path == "/telemetry" else b"{}")

                if asynchronous:

                    async def run():
                        async def hook(response):
                            if response.request.url.path != "/telemetry":
                                self.assertEqual((await underlying.get("/telemetry")).status_code, 200)

                        async with httpx.AsyncClient(
                            base_url="https://example.test",
                            transport=httpx.MockTransport(handle),
                            event_hooks={"response": [hook]},
                        ) as underlying:
                            client = Client(
                                base_url="https://example.test", max_response_bytes=16
                            ).set_async_httpx_client(underlying)
                            self.assertEqual(
                                (await get_api_v1_admin_openapi_json.asyncio_detailed(client=client)).status_code, 200
                            )

                    asyncio.run(run())
                else:

                    def hook(response):
                        if response.request.url.path != "/telemetry":
                            self.assertEqual(underlying.get("/telemetry").status_code, 200)

                    with httpx.Client(
                        base_url="https://example.test",
                        transport=httpx.MockTransport(handle),
                        event_hooks={"response": [hook]},
                    ) as underlying:
                        client = Client(base_url="https://example.test", max_response_bytes=16).set_httpx_client(
                            underlying
                        )
                        self.assertEqual(get_api_v1_admin_openapi_json.sync_detailed(client=client).status_code, 200)

    def test_response_limit_must_be_positive(self):
        for limit in (0, -1, True, None):
            with self.assertRaises(ValueError):
                Client(base_url="https://example.test", max_response_bytes=limit)
