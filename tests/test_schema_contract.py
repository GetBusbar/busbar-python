import asyncio
import importlib
import json
import unittest
from pathlib import Path

import httpx

from busbar_admin import AuthenticatedClient
from busbar_admin.api.default import get_plugins, post_api_v1_admin_keys, post_keys, put_admin_auth
from busbar_admin.models import CreateKeyReq, Error, HookStatusView, HookView, KeyView, PutAuthBody


def key_metadata():
    return {
        "id": "key-1",
        "name": "test",
        "allowed_pools": None,
        "group": None,
        "enabled": True,
        "created_at": 1,
        "labels": {},
        "state": "active",
    }


def hook_status():
    return {
        "name": "hook",
        "desired": {"settings_keys": ["token"], "settings_version": 1},
        "reported": None,
        "drift": None,
        "drift_keys": [],
        "metrics": [],
        "as_of": 1,
        "source": "live",
    }


class SchemaContract(unittest.TestCase):
    def test_key_creation_transmits_body_and_parses_current_signed_token(self):
        seen = []
        payload = {**key_metadata(), "token": "once-secret", "expires_at": 99, "group_provisioned": False}

        def handle(request):
            seen.append(request)
            self.assertEqual(request.headers["authorization"], "Bearer admin")
            return httpx.Response(201, json=payload)

        with AuthenticatedClient(
            base_url="https://example.test", token="admin", httpx_args={"transport": httpx.MockTransport(handle)}
        ) as client:
            result = post_api_v1_admin_keys.sync(client=client, body=CreateKeyReq(name="test", allowed_pools=None))
        self.assertIs(post_api_v1_admin_keys.sync, post_keys.sync)
        body = json.loads(seen[0].content)
        self.assertEqual(body["name"], "test")
        self.assertIsNone(body["allowed_pools"])
        self.assertEqual(seen[0].headers["content-type"], "application/json")
        self.assertEqual(result.token, "once-secret")
        self.assertIsNone(result.allowed_pools)
        self.assertNotIn("once-secret", repr(result))
        self.assertEqual(KeyView.from_dict(key_metadata()).state, "active")

    def test_async_admin_auth_body_preserves_explicit_empty_chain(self):
        seen = []

        def handle(request):
            seen.append(json.loads(request.content))
            self.assertEqual(request.headers["authorization"], "Bearer admin")
            return httpx.Response(
                200, json={"configured": False, "modules": [], "applied": True, "config_version": 2, "note": "open"}
            )

        async def run():
            async with AuthenticatedClient(
                base_url="https://example.test", token="admin", httpx_args={"transport": httpx.MockTransport(handle)}
            ) as client:
                return await put_admin_auth.asyncio(client=client, body=PutAuthBody(admin_auth=[]))

        result = asyncio.run(run())
        self.assertEqual(seen, [{"admin_auth": []}])
        self.assertFalse(result.configured)
        self.assertEqual(result.modules, [])

    def test_hook_projections_parse_key_names_and_drift(self):
        status = HookStatusView.from_dict(hook_status())
        self.assertEqual(status.desired.settings_keys, ["token"])
        self.assertIsNone(status.reported)
        self.assertEqual(status.drift_keys, [])
        hook = HookView.from_dict(
            {
                "name": "hook",
                "kind": "tap",
                "transport": {"kind": "none", "target": None},
                "prompt": "no",
                "user": "no",
                "priority": 0,
                "on_error": "nothing",
                "on_empty": None,
                "signals": ["requested_model", "latency"],
                "default": True,
                "timeout_ms": 1000,
                "settings_keys": ["token"],
                "global": False,
                "phase": [],
                "fires_at": ["request"],
                "groups": [],
            }
        )
        self.assertEqual(hook.settings_keys, ["token"])
        self.assertEqual(hook.fires_at, ["request"])
        self.assertIsNone(hook.to_dict()["on_empty"])
        self.assertEqual(hook.to_dict()["signals"], ["requested_model", "latency"])
        self.assertIs(hook.to_dict()["default"], True)
        self.assertNotIn("at", hook.to_dict())

    def test_documented_error_envelopes_are_preserved(self):
        for status in (400, 500):
            with self.subTest(status=status):
                payload = {"error": {"code": "invalid_request" if status == 400 else "internal", "message": "failure"}}
                with AuthenticatedClient(
                    base_url="https://example.test",
                    token="admin",
                    httpx_args={"transport": httpx.MockTransport(lambda request: httpx.Response(status, json=payload))},
                ) as client:
                    result = get_plugins.sync(client=client, type_="invalid")
                self.assertIsInstance(result, Error)
                self.assertEqual(result.error.code.value, payload["error"]["code"])

    def test_nullable_models_reject_malformed_present_objects(self):
        payload = hook_status()
        payload["reported"] = {"settings_keys": []}
        with self.assertRaises(ValueError):
            HookStatusView.from_dict(payload)

    def test_removed_key_limits_are_not_silently_discarded(self):
        with self.assertRaises(ValueError):
            CreateKeyReq.from_dict({"name": "limited", "rpm_limit": 1})

    def test_established_endpoint_modules_remain_importable(self):
        directory = Path(__file__).parents[1] / "busbar_admin/api/default"
        aliases = list(directory.glob("*_api_v1_admin_*.py"))
        self.assertEqual(len(aliases), 37)
        for path in aliases:
            module = importlib.import_module("busbar_admin.api.default." + path.stem)
            self.assertTrue(callable(module.sync_detailed))
            self.assertTrue(callable(module.asyncio_detailed))
