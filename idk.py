import string
import random
alphabets = string.ascii_lowercase
#print(len(alphabets))


# for i in range(1, 10): #going to generate ten words
#     word = ""
#     for j in range(1, random.randint(5, 10)):
#         letter = alphabets[random.randint(0, 25)]
#         word += letter
#     print(word)



alphabets = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

# Generates 9 random words
for i in range(1, 10):
    word = ""
    # Choose a random length for the word between 3 and 9
    word_length = random.randint(3, 9)
    
    for j in range(word_length):
        letter = random.choice(alphabets)
        
        # If the word has letters, check if both the last letter and the new letter are vowels
        if len(word) > 0 and letter in vowels and word[-1] in vowels:
            # Pick a random letter until it is NOT a vowel (a consonant)
            while letter in vowels:
                letter = random.choice(alphabets)
                
        word += letter
    print(word)
