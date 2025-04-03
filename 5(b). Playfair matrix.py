def create_playfair_matrix():
    return [
        ['M', 'F', 'H', 'I', 'J', 'K'],
        ['U', 'N', 'O', 'P', 'Q'],
        ['Z', 'V', 'W', 'X', 'Y'],
        ['E', 'L', 'A', 'R', 'G'],
        ['D', 'S', 'T', 'B', 'C']
    ]
def find_position(matrix, letter):
    """Find row and column of a letter in the Playfair matrix."""
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter or (letter in ['I', 'J'] and matrix[row][col] in ['I', 'J']):
                return row, col
    return None
def encrypt_playfair(text, matrix):
    """Encrypt text using Playfair cipher matrix."""
    text = text.upper().replace('J', 'I')  # Convert to uppercase and replace J with I
    encrypted_text = ""
    for i in range(0, len(text), 2):
        if i + 1 >= len(text):
            text += 'X'  # Padding if last letter is alone
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        # Same row: shift right
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        # Same column: shift down
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        # Rectangle swap
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return encrypted_text
# Example Usage
playfair_matrix = create_playfair_matrix()
plaintext = "HELLO"
ciphertext = encrypt_playfair(plaintext, playfair_matrix)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
