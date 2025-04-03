from Crypto.Cipher import DES
import binascii
def left_shift(bits, n):
    """Perform a left shift of n positions on the bits."""
    return bits[n:] + bits[:n]
def generate_subkeys(key):
    """Generate 16 DES-like subkeys according to the modified rules."""
    # Step 1: Convert key into binary format
    key = bin(int(binascii.hexlify(key), 16))[2:].zfill(56)  # 56 bits (without parity)
    # Step 2: Split the key into two 28-bit halves
    C = key[:28]
    D = key[28:]
    # Generate subkeys (first 24 bits from one subset, second 24 bits from a disjoint subset)
    subkeys = []
    for round in range(16):
        # Perform a left shift on C and D
        C = left_shift(C, 1)
        D = left_shift(D, 1)
        # The first 24 bits of the subkey come from the first half (C), and the next 24 bits from the second half (D)
        subkey = C[:24] + D[:24]
        # Append the subkey
        subkeys.append(subkey)
    return subkeys
def display_subkeys(subkeys):
    """Display subkeys as hex strings."""
    for i, subkey in enumerate(subkeys):
        hex_subkey = hex(int(subkey, 2))[2:].zfill(12)  # 12 hex characters for each subkey
        print(f"Subkey {i+1}: {hex_subkey}")
# Example usage
if __name__ == "__main__":
    # Example 56-bit key (must be 7 bytes in hex format without parity bits)
    key = binascii.unhexlify("0133457799BBCDFF")  # 56-bit key
    subkeys = generate_subkeys(key)
    display_subkeys(subkeys)
