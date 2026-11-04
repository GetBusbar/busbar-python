import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check-generated.sh"


class GeneratedDrift(unittest.TestCase):
    def test_generated_changes_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", directory], check=True)
            package = root / "busbar_admin"
            package.mkdir()
            (package / "client.py").write_text("original\n")
            (root / "setup.py").write_text("original\n")
            (root / "GENERATED_CLIENT.md").write_text("original\n")
            subprocess.run(["git", "-C", directory, "add", "."], check=True)
            subprocess.run(
                ["git", "-C", directory, "-c", "core.hooksPath=/dev/null",
                 "-c", "user.name=Test", "-c",
                 "user.email=test@example.invalid", "commit", "-qm", "fixture"],
                check=True,
            )

            def check(expected):
                result = subprocess.run(["bash", str(SCRIPT)], cwd=root, capture_output=True)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)

            check(0)
            for path in [package / "new_wrapper.py", root / "GENERATED_CLIENT.md"]:
                with self.subTest(path=path.name):
                    original = path.read_bytes() if path.exists() else None
                    path.write_text("changed\n")
                    check(1)
                    subprocess.run(["git", "-C", directory, "add", str(path)], check=True)
                    check(1)
                    subprocess.run(["git", "-C", directory, "reset", "-q", "HEAD"], check=True)
                    if original is None:
                        path.unlink()
                    else:
                        path.write_bytes(original)
            (root / "unrelated.txt").write_text("unrelated\n")
            check(0)
            (package / "client.py").unlink()
            check(1)
