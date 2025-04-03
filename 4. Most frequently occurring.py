from collections import Counter
def frequency_analysis(ciphertext):
    freq = Counter(ciphertext)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq
# Example usage
ciphertext = "ZEBRAS ARE BEAUTIFUL ANIMALS"
freq_list = frequency_analysis(ciphertext.replace(" ", ""))
print("Letter frequencies:", freq_list)
