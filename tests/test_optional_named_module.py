import unittest

from busbar_admin.models import NamedDefView
from busbar_admin.types import UNSET


class OptionalNamedModule(unittest.TestCase):
    def test_module_free_definition_keeps_module_absent_on_round_trip(self):
        payload = {"name": "module-free-plane", "settings_keys": []}
        definition = NamedDefView.from_dict(payload)
        self.assertIs(definition.module, UNSET)
        self.assertNotIn("module", definition.to_dict())

    def test_plugin_definition_preserves_its_module(self):
        payload = {"name": "plugin-plane", "module": "llm", "settings_keys": []}
        definition = NamedDefView.from_dict(payload)
        self.assertEqual(definition.module, "llm")
        self.assertEqual(definition.to_dict()["module"], "llm")
