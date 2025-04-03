from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
iv = get_random_bytes(16)
block_size = 16
plaintext = b"HELLO WORLD AES!"
padded_plaintext = pad(plaintext, block_size)
ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_ciphertext = ecb_cipher.encrypt(padded_plaintext)
cbc_cipher = AES.new(key, AES.MODE_CBC, iv)
cbc_ciphertext = cbc_cipher.encrypt(padded_plaintext)
cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
cfb_ciphertext = cfb_cipher.encrypt(plaintext)
ecb_decipher = AES.new(key, AES.MODE_ECB)
cbc_decipher = AES.new(key, AES.MODE_CBC, iv)
cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
decrypted_ecb = unpad(ecb_decipher.decrypt(ecb_ciphertext), block_size)
decrypted_cbc = unpad(cbc_decipher.decrypt(cbc_ciphertext), block_size)
decrypted_cfb = cfb_decipher.decrypt(cfb_ciphertext)
print("ECB Ciphertext:", ecb_ciphertext.hex())
print("CBC Ciphertext:", cbc_ciphertext.hex())
print("CFB Ciphertext:", cfb_ciphertext.hex())
print("\nDecrypted ECB:", decrypted_ecb.decode())
print("Decrypted CBC:", decrypted_cbc.decode())
print("Decrypted CFB:", decrypted_cfb.decode())
