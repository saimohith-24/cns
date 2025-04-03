from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import binascii
def generate_key():
    """Generate a random 24-byte key for 3DES."""
    while True:
        key = get_random_bytes(24)
        try:
            DES3.adjust_key_parity(key)
            return key
        except ValueError:
            continue
def encrypt_cbc(plaintext, key):
    """Encrypt plaintext using 3DES in CBC mode."""
    iv = get_random_bytes(8)  # 3DES requires an 8-byte IV
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES3.block_size))
    return iv + ciphertext  # Prepend IV for decryption
if __name__ == "__main__":
    key = generate_key()
    plaintext = "Hello, World!"  # Example plaintext
    ciphertext = encrypt_cbc(plaintext, key)
    print("Encryption Key (hex):", binascii.hexlify(key).decode())
    print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode())
