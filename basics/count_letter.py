'''
Exercise 3: Count a Letter
Write a function that counts how many times a specified letter appears in a string, ignoring uppercase and lowercase.
'''

def count_letter(word,letter):
    count = 0
    for w in word:
        if w.lower() == letter.lower():
            count += 1
    return count
    
    
print(count_letter("Programming in Python", "p"))