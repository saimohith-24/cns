from collections import Counter
def letter_frequency_attack(ciphertext, top_n=10):
    # English letter frequency ordered by most common usage
    english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"    
    # Count letter frequencies in ciphertext
    cipher_counts = Counter(filter(str.isalpha, ciphertext))
    sorted_cipher_chars = [pair[0] for pair in cipher_counts.most_common()]
    # Generate possible plaintexts
    possible_plaintexts = []
    for shift in range(26):
        plaintext = ''.join(
            chr(((ord(char) - ord('A') - shift) % 26) + ord('A')) if char.isalpha()
            else char
            for char in ciphertext
        )
        possible_plaintexts.append((shift, plaintext))
    # Rank based on letter frequency similarity
    possible_plaintexts.sort(key=lambda x: sum(
        english_freq.index(c) if c in english_freq else 26 for c in x[1] if c.isalpha()
    ))
    return [text for _, text in possible_plaintexts[:top_n]]
# Example usage
if __name__ == "__main__":
    ciphertext = "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"
    top_plaintexts = letter_frequency_attack(ciphertext, top_n=10)    
    print("Top possible plaintexts:")
    for i, text in enumerate(top_plaintexts, 1):
        print(f"{i}: {text}")
