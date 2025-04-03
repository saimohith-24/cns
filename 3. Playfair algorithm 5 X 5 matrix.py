import numpy as np
# Create Playfair matrix
def create_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # Remove duplicates, replace J with I
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [c for c in key + "".join(c for c in alphabet if c not in key)]
    return np.array(matrix).reshape(5, 5)
# Find position of a letter in the matrix
def find_position(matrix, letter):
    pos = np.where(matrix == letter)
    return pos[0][0], pos[1][0]
# Encrypt a digraph using Playfair rules
def encrypt_digraph(matrix, digraph):
    a, b = digraph
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)    
    if row1 == row2:  # Same row
        return matrix[row1, (col1 + 1) % 5] + matrix[row2, (col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 + 1) % 5, col1] + matrix[(row2 + 1) % 5, col2]
    else:  # Rectangle swap
        return matrix[row1, col2] + matrix[row2, col1]
# Encrypt message
def playfair_encrypt(message, key):
    matrix = create_playfair_matrix(key)
    message = message.upper().replace("J", "I").replace(" ", "")
    if len(message) % 2 != 0:
        message += "X"  # Padding if odd length
    ciphertext = "".join(encrypt_digraph(matrix, message[i:i+2]) for i in range(0, len(message), 2))
    return ciphertext
# Example usage
key = "CIPHER"
plaintext = "MUSTSEEYOUOVERCADOGANWESTCOMINGATONCE"
ciphertext = playfair_encrypt(plaintext, key)
print("Playfair Ciphertext:", ciphertext)
