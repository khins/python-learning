'''
You’ll need two string methods:
.strip() removes spaces from the beginning and end.
.capitalize() makes the first character uppercase and the remaining characters lowercase.
'''

def clean_word(word):
    return word.strip().capitalize()

print(clean_word("  aLEX  "))
print(clean_word("JOHNSON"))
print(clean_word("  mArIa"))