import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class GenerationRecipe(unittest.TestCase):
    def test_generator_failure_preserves_installed_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copyfile(Path(__file__).parents[1] / "Makefile", root / "Makefile")
            (root / "busbar_admin").mkdir()
            source = root / "busbar_admin/__init__.py"
            source.write_text("original source\n")
            setup = root / "setup.py"
            setup.write_text("original setup\n")
            binary = root / "openapi-python-client"
            binary.write_text(
                '#!/bin/sh\nif [ "$1" = "--version" ]; then echo "openapi-python-client version: 0.29.1"; exit 0; fi\nexit 1\n'
            )
            binary.chmod(0o755)
            result = subprocess.run(
                ["make", "generate"],
                cwd=root,
                env={**os.environ, "PATH": f"{root}:{os.environ['PATH']}"},
                capture_output=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue(source.exists(), "generator failure deleted checked-in package")
            self.assertEqual(source.read_text(), "original source\n")
            self.assertEqual(setup.read_text(), "original setup\n")
