import numpy as np
from sympy import Matrix
from math import gcd
def mod_inverse_matrix(matrix, mod):
    """Compute the modular inverse of a matrix under mod."""
    matrix = Matrix(matrix)
    det = int(matrix.det())  # Compute determinant    
    if det == 0 or gcd(det, mod) != 1:
        raise ValueError(f"Matrix is not invertible under modulo {mod}")    
    return np.array(matrix.inv_mod(mod)).astype(int)
def known_plaintext_attack(plaintext_pairs, ciphertext_pairs, mod=26):
    """Recover the encryption key matrix using known plaintext attack."""
    P = np.array(plaintext_pairs)
    C = np.array(ciphertext_pairs)
    # Compute the modular inverse of P
    P_inv = mod_inverse_matrix(P, mod)
    # Compute the key matrix: K = C * P^(-1) mod 26
    K = (np.dot(C, P_inv) % mod).astype(int)
    return K
# Example plaintext-ciphertext pairs (assuming 2x2 key matrix for simplicity)
plaintext_pairs = [[7, 8], [11, 11]]  # Example known plaintext
ciphertext_pairs = [[19, 10], [5, 16]]  # Corresponding ciphertext
# Recover the key
try:
    key_matrix = known_plaintext_attack(plaintext_pairs, ciphertext_pairs)
    print("Recovered Key Matrix:")
    print(key_matrix)
except ValueError as e:
    print("Error:", e)
