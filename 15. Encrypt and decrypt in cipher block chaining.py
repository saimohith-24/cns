from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii
def binary_to_bytes(binary_str):
    return bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
def encrypt_cbc(plaintext_bin, key_bin, iv_bin):
    key = binary_to_bytes(key_bin)
    iv = binary_to_bytes(iv_bin)
    plaintext = binary_to_bytes(plaintext_bin)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    return ciphertext
def decrypt_cbc(ciphertext, key_bin, iv_bin):
    key = binary_to_bytes(key_bin)
    iv = binary_to_bytes(iv_bin)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_data
if __name__ == "__main__":
    key_bin = "0111111101".zfill(64)  # 10-bit key padded to 64-bit
    iv_bin = "10101010".zfill(64)  # 8-bit IV padded to 64-bit
    plaintext_bin = "0000000100100011".zfill(64)  # 16-bit plaintext padded to 64-bit
    ciphertext = encrypt_cbc(plaintext_bin, key_bin, iv_bin)
    decrypted_text = decrypt_cbc(ciphertext, key_bin, iv_bin)
    print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode())
    print("Decrypted Text (binary):", ''.join(format(byte, '08b') for byte in decrypted_text))
