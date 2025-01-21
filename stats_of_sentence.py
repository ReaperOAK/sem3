def count_stats(sentence):
    vowels = "aeiouAEIOU"
    punctuations = ".,;:!?\"'()-"
    num_words = len(sentence.split())
    num_vowels = sum(1 for char in sentence if char in vowels)
    num_consonants = sum(1 for char in sentence if char.isalpha() and char not in vowels)
    num_punctuations = sum(1 for char in sentence if char in punctuations)
    
    return num_words, num_vowels, num_consonants, num_punctuations

# Example usage
sentence = input("Enter a sentence: ")

num_words, num_vowels, num_consonants, num_punctuations = count_stats(sentence)
print(f"Number of words: {num_words}")
print(f"Number of vowels: {num_vowels}")
print(f"Number of consonants: {num_consonants}")
print(f"Number of punctuations: {num_punctuations}")