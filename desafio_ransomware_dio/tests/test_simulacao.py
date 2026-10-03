from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import decrypter
import encrypter


class RansomwareLabSimulationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.lab = self.root / "lab_data"
        self.lab.mkdir()

        self.original_lab_dir = encrypter.LAB_DIR
        self.original_key_file = encrypter.KEY_FILE
        self.original_dec_lab_dir = decrypter.LAB_DIR
        self.original_dec_key_file = decrypter.KEY_FILE

        encrypter.LAB_DIR = self.lab
        encrypter.KEY_FILE = self.lab / "lab_key.bin"
        decrypter.LAB_DIR = self.lab
        decrypter.KEY_FILE = self.lab / "lab_key.bin"

    def tearDown(self) -> None:
        encrypter.LAB_DIR = self.original_lab_dir
        encrypter.KEY_FILE = self.original_key_file
        decrypter.LAB_DIR = self.original_dec_lab_dir
        decrypter.KEY_FILE = self.original_dec_key_file
        self.tempdir.cleanup()

    def test_round_trip(self) -> None:
        target = self.lab / "teste.txt"
        original = "conteúdo sintético para teste"
        target.write_text(original, encoding="utf-8")

        key = encrypter.create_key()
        locked = encrypter.encrypt_file(target, key)
        restored = decrypter.decrypt_file(locked, key)

        self.assertTrue(locked.exists())
        self.assertTrue(restored.exists())
        self.assertEqual(restored.read_text(encoding="utf-8"), original)

    def test_key_is_256_bits(self) -> None:
        key = encrypter.create_key()
        self.assertEqual(len(key), 32)
        self.assertEqual(encrypter.create_key(), key)

    def test_path_escape_is_rejected(self) -> None:
        outside = self.root / "fora.txt"
        outside.write_text("não deve ser tocado", encoding="utf-8")
        key = encrypter.create_key()

        with self.assertRaises(ValueError):
            encrypter.encrypt_file(outside, key)

    def test_locked_format_is_not_plaintext(self) -> None:
        target = self.lab / "dados.txt"
        plaintext = "dados de laboratório".encode("utf-8")
        target.write_bytes(plaintext)

        key = encrypter.create_key()
        locked = encrypter.encrypt_file(target, key)

        self.assertNotIn(plaintext, locked.read_bytes())


if __name__ == "__main__":
    unittest.main()
