import os
import sys
import logging
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.exceptions import InvalidTag

_cipher = None

def init_cipher(password: str, data_dir: str):
    global _cipher
    salt_path = os.path.join(data_dir, "crypto.salt")
    
    if os.path.exists(salt_path):
        with open(salt_path, "rb") as f:
            salt = f.read()
    else:
        salt = os.urandom(16)
        os.makedirs(data_dir, exist_ok=True)
        with open(salt_path, "wb") as f:
            f.write(salt)
            
    # Key: 256-bits
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )
    key = kdf.derive(password.encode('utf-8'))
    _cipher = AESGCM(key)

def encrypt_data(data: bytes) -> bytes:
    if not _cipher:
        raise RuntimeError("A titkosító kulcs nincs inicializálva!")
    nonce = os.urandom(12) # GCM standard nonce size
    return nonce + _cipher.encrypt(nonce, data, None)

def decrypt_data(data: bytes) -> bytes:
    if not _cipher:
        raise RuntimeError("A titkosító kulcs nincs inicializálva!")
    nonce = data[:12]
    ciphertext = data[12:]
    try:
        return _cipher.decrypt(nonce, ciphertext, None)
    except InvalidTag:
        raise ValueError("Hibás jelszó vagy sérült fájl!")
