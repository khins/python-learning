'''
count_words.py
Exercise 11: Count Words Reliably
Write a function named count_words that returns the number
 of words in a sentence, even when it contains irregular spacing.
 Requirements:
Use string methods.
Do not use a loop.
Return an integer.
Handle empty and whitespace-only strings correctly.
'''
def count_words(word):
    word_count = word.split()
    return len(word_count)
    
 

print(count_words("Python string methods are useful"))       # 5)
print(count_words("   Python   makes   text   easier   "))   # 4
print(count_words(""))                                      # 0
print(count_words("      "))                                # 0