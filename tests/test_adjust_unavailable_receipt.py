import unittest

import httpx

from busbar_admin import AuthenticatedClient
from busbar_admin.api.default import post_adjust
from busbar_admin.models import AdjustmentActionView, Error


class AdjustmentUnavailableReceipt(unittest.TestCase):
    def test_503_preserves_known_not_applied_receipt(self):
        payload = {
            "operation": "adjust",
            "operation_id": "action-1",
            "actor": "operator",
            "target": "key-1",
            "fingerprint": "request-hash",
            "reason_hash": "reason-hash",
            "effect": "not_applied",
            "applied": False,
            "recovery": "receipt",
            "retry": "same_action_only",
            "count_scale": 6,
        }
        response = httpx.Response(
            503,
            json=payload,
            headers={"x-busbar-adjust-effect": "not_applied", "x-busbar-receipt-durable": "false"},
        )
        client = AuthenticatedClient(base_url="https://example.test", token="admin")
        result = post_adjust._parse_response(client=client, response=response)
        self.assertIsInstance(result, AdjustmentActionView)
        self.assertEqual(result.effect, "not_applied")
        self.assertFalse(result.applied)
        self.assertEqual(result.recovery, "receipt")
        self.assertEqual(result.retry, "same_action_only")
        detailed = post_adjust._build_response(client=client, response=response)
        self.assertEqual(detailed.status_code, 503)
        self.assertEqual(detailed.headers["x-busbar-adjust-effect"], "not_applied")
        self.assertEqual(detailed.headers["x-busbar-receipt-durable"], "false")

    def test_503_preserves_ordinary_unavailable_error(self):
        response = httpx.Response(503, json={"error": {"code": "unavailable", "message": "preparation failed"}})
        client = AuthenticatedClient(base_url="https://example.test", token="admin")
        result = post_adjust._parse_response(client=client, response=response)
        self.assertIsInstance(result, Error)
        self.assertEqual(result.error.code, "unavailable")
