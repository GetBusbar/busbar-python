import unittest

import httpx

from busbar_admin import Client
from busbar_admin.api.default import get_usage
from busbar_admin.models import ObservationUsageView, UsageView
from busbar_admin.types import UNSET


class ObservationUsage(unittest.TestCase):
    def test_exact_observation_strings_and_omission(self):
        observation = {
            "key_id": "key-1",
            "group": "team",
            "instance": "gateway",
            "destination": "provider",
            "serving_subject": "requested-model",
            "rated_subject": "billed-model",
            "accounting_time": "18446744073709551615",
            "counts": {"duration": "170141183460469231731687303715884.105727", "requests": "0.000001"},
            "spend_micros": "9223372036854775.807",
        }
        for present in (True, False):
            with self.subTest(observations=present):
                payload = {
                    "window": {"start": 0, "end": 1},
                    "as_of": 1,
                    "currency": "USD",
                    "rate_card_version": None,
                    "total": {
                        "tokens_input": 0,
                        "tokens_output": 0,
                        "tokens_cache_read": 0,
                        "tokens_cache_creation": 0,
                        "requests": 0,
                        "spend_micros": 0,
                    },
                    "by_model": [],
                    "by_key": [],
                    "by_key_truncated": False,
                }
                if present:
                    payload["observations"] = [observation]
                with Client(
                    base_url="https://admin.example",
                    httpx_args={"transport": httpx.MockTransport(lambda request: httpx.Response(200, json=payload))},
                ) as client:
                    usage = get_usage.sync(client=client)
                self.assertIsInstance(usage, UsageView)
                self.assertEqual("observations" in usage.to_dict(), present)
                if present:
                    self.assertIsInstance(usage.observations[0], ObservationUsageView)
                    self.assertEqual(usage.to_dict()["observations"], [observation])
                else:
                    self.assertIs(usage.observations, UNSET)
