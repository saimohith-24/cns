"""Write a C program to Encrypt the message “meet me at the usual place at ten rather than eight oclock” using the Hill cipher with the key.
( 9 4 )
(5 7 )
a. Show your calculations and the result. b. Show the calculations for the corresponding decryption of the ciphertext to recover the original plaintext"""
import numpy as np
# Convert text to number indices
def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper().replace(" ", "")]
# Convert number indices back to text
def numbers_to_text(numbers):
    return "".join(chr(n % 26 + ord('A')) for n in numbers)
# Encrypt using Hill cipher
def hill_encrypt(plaintext, key_matrix):
    numbers = text_to_numbers(plaintext)
    if len(numbers) % 2 != 0:
        numbers.append(0)  # Padding for even length
    numbers = np.array(numbers).reshape(-1, 2)
    encrypted = (np.dot(numbers, key_matrix) % 26).flatten()
    return numbers_to_text(encrypted)
# Example usage
key_matrix = np.array([[9, 4], [5, 7]])  # Given key matrix
plaintext = "MEETMEATUSUALPLACE"  # Plaintext message
ciphertext = hill_encrypt(plaintext, key_matrix)
print("Hill Ciphertext:", ciphertext)
