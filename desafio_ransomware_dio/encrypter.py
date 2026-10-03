"""Criptografador de laboratório para o desafio de Cybersecurity da DIO.

ATENÇÃO: este script foi projetado para uma simulação controlada.
Ele só pode operar em arquivos dentro de ./lab_data.
"""

from __future__ import annotations

import base64
import os
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

BASE_DIR = Path(__file__).resolve().parent
LAB_DIR = BASE_DIR / "lab_data"
KEY_FILE = LAB_DIR / "lab_key.bin"
LOCKED_SUFFIX = ".locked"


def _safe_lab_path(path: Path) -> Path:
    """Resolve um caminho e garante que ele está dentro do laboratório."""
    candidate = path.resolve()
    lab_root = LAB_DIR.resolve()
    if candidate == lab_root or lab_root not in candidate.parents:
        raise ValueError("Operação bloqueada: arquivo fora do diretório de laboratório.")
    return candidate


def create_key() -> bytes:
    """Cria uma chave AES-256 para o laboratório ou reutiliza a existente."""
    LAB_DIR.mkdir(exist_ok=True)
    if KEY_FILE.exists():
        key = KEY_FILE.read_bytes()
        if len(key) != 32:
            raise ValueError("A chave do laboratório deve possuir 32 bytes.")
        return key

    key = AESGCM.generate_key(bit_length=256)
    KEY_FILE.write_bytes(key)
    return key


def encrypt_file(path: Path, key: bytes) -> Path:
    """Criptografa um arquivo do laboratório e preserva o original."""
    path = _safe_lab_path(path)
    if path.name == KEY_FILE.name or path.suffix == LOCKED_SUFFIX:
        raise ValueError("Arquivo não elegível para a simulação.")

    plaintext = path.read_bytes()
    nonce = os.urandom(12)
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, None)
    output = path.with_name(path.name + LOCKED_SUFFIX)
    output.write_bytes(b"DIO-LAB1" + nonce + ciphertext)
    return output


def main() -> None:
    LAB_DIR.mkdir(exist_ok=True)
    key = create_key()
    candidates = sorted(
        p for p in LAB_DIR.iterdir()
        if p.is_file() and p.name != KEY_FILE.name and p.suffix != LOCKED_SUFFIX
    )

    if not candidates:
        print("Nenhum arquivo de demonstração encontrado em lab_data/.")
        return

    print("=== Simulação de criptografia controlada ===")
    print(f"Diretório permitido: {LAB_DIR}")
    print(f"Arquivos encontrados: {len(candidates)}")

    for path in candidates:
        output = encrypt_file(path, key)
        print(f"[OK] {path.name} -> {output.name}")

    print("Chave do laboratório salva em lab_data/lab_key.bin")
    print("Nenhum arquivo original foi apagado.")


if __name__ == "__main__":
    main()
