import tempfile
import unittest
from pathlib import Path

from source_archive import write_source_archive


class SourceArchiveTests(unittest.TestCase):
    def test_record_boundaries_and_utf8_round_trip(self):
        lines = ['{"word":"词根"}\n', '{"word":"root"}\n', '{}\n']
        with tempfile.TemporaryDirectory() as folder:
            paths = write_source_archive(lines, folder, max_bytes=24)
            self.assertGreater(len(paths), 1)
            self.assertEqual(b''.join(p.read_bytes() for p in paths),
                             ''.join(lines).encode('utf-8'))
            self.assertTrue(all(p.stat().st_size <= 24 for p in paths))
            self.assertTrue(all(p.read_bytes().endswith(b'\n') for p in paths))

    def test_regeneration_removes_stale_parts(self):
        with tempfile.TemporaryDirectory() as folder:
            write_source_archive([b'{}\n'] * 3, folder, max_bytes=3)
            paths = write_source_archive([b'{}\n'], folder, max_bytes=3)
            self.assertEqual(sorted(Path(folder).glob('*.jsonl')), paths)

    def test_oversized_record_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError):
                write_source_archive([b'12345\n'], folder, max_bytes=3)


if __name__ == '__main__':
    unittest.main()
