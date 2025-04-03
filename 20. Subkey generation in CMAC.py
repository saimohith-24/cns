from Crypto.Cipher import AES, DES
import binascii
def left_shift(data):
    """Left shift a byte sequence by 1 bit, handling overflow correctly."""
    num = int.from_bytes(data, 'big') << 1  
    num &= (1 << (len(data) * 8)) - 1  
    return num.to_bytes(len(data), 'big')  
def generate_cmac_subkeys(cipher, key, block_size):
    """Generate two CMAC subkeys (K1, K2)."""
    zero_block = bytes(block_size)  
    cipher_obj = cipher.new(key, cipher.MODE_ECB)  
    L = cipher_obj.encrypt(zero_block)  
    Rb = {16: 0x87, 8: 0x1B}[block_size]
    K1 = left_shift(L)
    if L[0] & 0x80:  # If MSB is 1, XOR with Rb
        K1 = (int.from_bytes(K1, 'big') ^ Rb).to_bytes(block_size, 'big')
    K2 = left_shift(K1)
    if K1[0] & 0x80:
        K2 = (int.from_bytes(K2, 'big') ^ Rb).to_bytes(block_size, 'big')
    return K1, K2
aes_key = b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\xcf\x15\x88\x09\xcf\x4f'  # 16-byte AES key
des_key = b'\x13\x34\x57\x79\x9B\xBC\xDF\xF1'  # 8-byte DES key
K1_aes, K2_aes = generate_cmac_subkeys(AES, aes_key, 16)
print("AES CMAC Subkeys:")
print("K1:", binascii.hexlify(K1_aes))
print("K2:", binascii.hexlify(K2_aes))
K1_des, K2_des = generate_cmac_subkeys(DES, des_key, 8)
print("\nDES CMAC Subkeys:")
print("K1:", binascii.hexlify(K1_des))
print("K2:", binascii.hexlify(K2_des))
