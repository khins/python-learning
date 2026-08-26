# Define a long_word function that accepts a string. 
# The function should return a Boolean that reflects whether the string has more than 7 characters.
# 
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True

def long_word(word):
    if len(word) > 7:
        return True
    else:
        return False
        
print(long_word("Python"))
print(long_word("magnificent"))