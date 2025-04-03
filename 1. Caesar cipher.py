def caesar_cipher(text, k, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift = k if encrypt else -k
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result
# Example usage
text = input("Enter text: ")
k = int(input("Enter shift (1-25): "))
while not (1 <= k <= 25):
    print("Shift value must be between 1 and 25.")
    k = int(input("Enter shift (1-25): "))
encrypted_text = caesar_cipher(text, k, encrypt=True)
print(f"Encrypted: {encrypted_text}")
decrypted_text = caesar_cipher(encrypted_text, k, encrypt=False)
print(f"Decrypted: {decrypted_text}")
