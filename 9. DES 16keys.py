from Crypto.Cipher import DES
import binascii
def generate_des_keys(initial_key):
    # Placeholder for key schedule generation (simplified version)
    keys = [initial_key] * 16  # Simplified, actual DES key scheduling applies shifts
    return keys[::-1]  # Reverse for decryption
def des_decrypt(ciphertext, key):
    # Convert key and ciphertext from hex to bytes
    key = binascii.unhexlify(key)
    ciphertext = binascii.unhexlify(ciphertext)
    # Generate decryption keys in reverse order
    keys = generate_des_keys(key)
    # Initialize DES cipher in ECB mode with the first decryption key
    des = DES.new(keys[0], DES.MODE_ECB)
    # Perform decryption
    decrypted_text = des.decrypt(ciphertext)
    # Ensure the result is a valid string (strip padding)
    return decrypted_text.decode('utf-8', errors='ignore').strip()
# Example usage
if __name__ == "__main__":
    # Example 64-bit key (must be 8 bytes in hex format)
    key = "133457799BBCDFF1"
    # Example 64-bit ciphertext (must be 8 bytes in hex format)
    ciphertext = "85E813540F0AB405"
    decrypted_text = des_decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
