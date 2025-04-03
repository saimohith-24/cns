from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
def xor_bytes(a, b):
    """XOR two byte sequences."""
    return bytes(x ^ y for x, y in zip(a, b))
def generate_cbc_mac(key, message, block_size=16):
    """Compute CBC-MAC of a one-block message."""
    cipher = AES.new(key, AES.MODE_CBC, iv=b'\x00' * block_size)
    padded_msg = pad(message, block_size)
    mac = cipher.encrypt(padded_msg)[-block_size:]
    return mac
key = os.urandom(16)
message = b"HELLO BLOCK!"  
T = generate_cbc_mac(key, message)
new_message = message + xor_bytes(message, T)
new_mac = generate_cbc_mac(key, new_message)
print("MAC for X:", T.hex())
print("MAC for X || (X ⊕ T):", new_mac.hex())
