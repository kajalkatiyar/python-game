def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
letter = input("Enter a letter:")
print(is_vowel(letter))
