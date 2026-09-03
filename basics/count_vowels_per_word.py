'''
count_vowels_per_word.py
Nested Loops: Count Vowels per Word
Write count_vowels_per_word(words) that returns one vowel count for every word.
Structure to think through:
create result list

for each word:
    reset its vowel count
    for each character in that word:
        check whether it is a vowel
    append that word’s completed count
'''
def count_vowels_per_word(words):
    mylist = []
    vowel_count = 0

    for w in words:
        vowel_count = 0
        for char in w:
            if char.lower() in "aeiou":
                vowel_count += 1
        mylist.append(vowel_count)
    return mylist


print(count_vowels_per_word(["apple", "sky", "Education"]))
# [2, 0, 5]

print(count_vowels_per_word(["AEIOU", "rhythm", "Python"]))
# [5, 0, 1]

print(count_vowels_per_word(["", "a", ""]))
# [0, 1, 0]

print(count_vowels_per_word([]))
# []