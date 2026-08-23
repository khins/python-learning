'''
Start by breaking the problem into two operations:
Split the name into individual words.
Rejoin those words with exactly one space.
Python’s .split() is especially useful because, with no argument, it automatically ignores leading, trailing, and repeated spaces:
'''

def clean_name(name):
    words = name.split()
    # Capitalize each word
    for word in words:
        print(word)

    # Join the words and return the result
    
    


clean_name("  aLEX   johnSON  ")  # "Alex Johnson"