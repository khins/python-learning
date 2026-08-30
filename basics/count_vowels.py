'''
count_vowels.py
Control Flow Exercise 3: Count Vowels with a for Loop
Write count_vowels(text) that returns the total number of vowels in a string.
Treat these as vowels:
a, e, i, o, u
Requirements:
Ignore capitalization.
Use a for loop.
Use an accumulator variable starting at 0.
Do not use .count().
'''
def count_vowels(word):
    
    count_of_vowel = 0

    for letter in word.lower():
        if letter in "aeiou":
            count_of_vowel += 1 

    return count_of_vowel



print(count_vowels("Python"))              # 1
print(count_vowels("Education"))           # 5
print(count_vowels("AEIOU"))               # 5
print(count_vowels("rhythm"))               # 0
print(count_vowels(""))                     # 0
print(count_vowels("Hello, World! 123"))    # 3

# Correct. This version is concise and idiomatic while still making the loop logic easy to follow.