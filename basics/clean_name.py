'''
Start by breaking the problem into two operations:
Split the name into individual words.
Rejoin those words with exactly one space.
Python’s .split() is especially useful because, with no argument, it automatically ignores leading, trailing, and repeated spaces:
'''

def clean_name(name):
    #word = name.split()
    #cleaned_words = [w.strip().capitalize() for w in word]
    cleaned_words = []
    words = name.split()
    
    for word in words:
        clean_word = word.capitalize()
        cleaned_words.append(clean_word)
    return ' '.join(cleaned_words)

print(clean_name("  aLEX   johnSON  "))  # "Alex Johnson"