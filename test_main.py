import hashlib
import tempfile
import unittest
from pathlib import Path

from main import inventory, sha256_file, write_csv


class ForensicInventoryTests(unittest.TestCase):
    def test_sha256_matches_expected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.txt"
            path.write_text("evidence sample", encoding="utf-8")

            expected = hashlib.sha256(b"evidence sample").hexdigest()

            self.assertEqual(sha256_file(path), expected)

    def test_inventory_includes_nested_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source"
            (source / "nested").mkdir(parents=True)
            (source / "nested" / "sample.txt").write_text(
                "test", encoding="utf-8"
            )

            records = inventory(source)

            self.assertEqual(len(records), 1)
            self.assertEqual(
                Path(records[0]["caminho_relativo"]).as_posix(),
                "nested/sample.txt",
            )
            self.assertEqual(records[0]["status"], "OK")

    def test_csv_is_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source"
            source.mkdir()
            (source / "a.txt").write_text("A", encoding="utf-8")

            output = Path(tmp) / "reports" / "inventory.csv"

            write_csv(inventory(source), output)

            self.assertTrue(output.exists())
            self.assertIn(
                "sha256",
                output.read_text(encoding="utf-8-sig"),
            )


if __name__ == "__main__":
    unittest.main()
