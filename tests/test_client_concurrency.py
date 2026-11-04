import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch

from busbar_admin import AuthenticatedClient, Client


class ClientConcurrency(unittest.TestCase):
    def test_lazy_transport_is_constructed_once(self):
        for cls in (Client, AuthenticatedClient):
            for asynchronous in (False, True):
                with self.subTest(client=cls.__name__, asynchronous=asynchronous):
                    kwargs = {"token": "token"} if cls is AuthenticatedClient else {}
                    client = cls(base_url="https://example.test", **kwargs)
                    rendezvous = threading.Barrier(2)
                    created = []

                    def construct(**options):
                        value = object()
                        created.append(value)
                        try:
                            rendezvous.wait(timeout=0.2)
                        except threading.BrokenBarrierError:
                            pass
                        return value

                    getter = client.get_async_httpx_client if asynchronous else client.get_httpx_client
                    target = (
                        "busbar_admin.client.httpx.AsyncClient" if asynchronous else "busbar_admin.client.httpx.Client"
                    )
                    with patch(target, side_effect=construct), ThreadPoolExecutor(max_workers=2) as executor:
                        first = executor.submit(getter)
                        second = executor.submit(getter)
                        self.assertIs(first.result(), second.result())
                    self.assertEqual(len(created), 1)
