from sympy import mod_inverse
def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a must be coprime with 26 for the cipher to be one-to-one.")
    cipher = ""
    for char in text.upper():
        if char.isalpha():
            p = ord(char) - ord('A')
            C = (a * p + b) % 26      
            cipher += chr(C + ord('A'))
        else:
            cipher += char
    return cipher
def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    plain = ""
    for char in cipher:
        if char.isalpha():
            C = ord(char) - ord('A')
            p = (a_inv * (C - b)) % 26  
            plain += chr(p + ord('A'))
        else:
            plain += char
    return plain
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
a, b = 5, 8  
plaintext = "HELLO WORLD"
ciphertext = affine_encrypt(plaintext, a, b)
decrypted_text = affine_decrypt(ciphertext, a, b)
print("Affine Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
