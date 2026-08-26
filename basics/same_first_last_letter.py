# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner")   => True
# same_first_and_last_letter("Runner")   => False
# same_first_and_last_letter("clock")    => False
# same_first_and_last_letter("q")        => True

from sqlalchemy import false


def same_first_and_last_letter(word):
    if word[0] == word[-1]:
        return True  
    else:    
        return False
    
print(f'The first and last letters are the same: {same_first_and_last_letter("runner")}')
print(same_first_and_last_letter("clock"))
print(same_first_and_last_letter("q"))