"""Descriptografador de laboratório para o desafio de Cybersecurity da DIO.

ATENÇÃO: este script foi projetado para uma simulação controlada.
Ele só pode operar em arquivos dentro de ./lab_data.
"""

from __future__ import annotations

from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

BASE_DIR = Path(__file__).resolve().parent
LAB_DIR = BASE_DIR / "lab_data"
KEY_FILE = LAB_DIR / "lab_key.bin"
LOCKED_SUFFIX = ".locked"
MAGIC = b"DIO-LAB1"


def _safe_lab_path(path: Path) -> Path:
    candidate = path.resolve()
    lab_root = LAB_DIR.resolve()
    if candidate == lab_root or lab_root not in candidate.parents:
        raise ValueError("Operação bloqueada: arquivo fora do diretório de laboratório.")
    return candidate


def load_key() -> bytes:
    if not KEY_FILE.exists():
        raise FileNotFoundError("Chave do laboratório não encontrada.")
    key = KEY_FILE.read_bytes()
    if len(key) != 32:
        raise ValueError("A chave do laboratório deve possuir 32 bytes.")
    return key


def decrypt_file(path: Path, key: bytes) -> Path:
    """Descriptografa um arquivo .locked do laboratório e cria a cópia restaurada."""
    path = _safe_lab_path(path)
    if path.name == KEY_FILE.name or path.suffix != LOCKED_SUFFIX:
        raise ValueError("Arquivo não elegível para a simulação.")

    payload = path.read_bytes()
    if not payload.startswith(MAGIC) or len(payload) <= len(MAGIC) + 12:
        raise ValueError("Formato de laboratório inválido.")

    nonce_start = len(MAGIC)
    nonce = payload[nonce_start:nonce_start + 12]
    ciphertext = payload[nonce_start + 12:]
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)

    output = path.with_name(path.name[: -len(LOCKED_SUFFIX)])
    output.write_bytes(plaintext)
    return output


def main() -> None:
    key = load_key()
    candidates = sorted(LAB_DIR.glob(f"*{LOCKED_SUFFIX}"))

    if not candidates:
        print("Nenhum arquivo .locked encontrado em lab_data/.")
        return

    print("=== Simulação de recuperação de arquivos ===")
    for path in candidates:
        output = decrypt_file(path, key)
        print(f"[OK] {path.name} -> {output.name}")

    print("Arquivos de demonstração restaurados com a chave do laboratório.")


if __name__ == "__main__":
    main()
