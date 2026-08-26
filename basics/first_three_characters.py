
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty")   => "dyn"
# first_three_characters("empire")    => "emp"

def first_three_characters(word):
    return word[0:3]
    
print(first_three_characters("dynasty"))  # => "dyn"
print(first_three_characters("empire"))   # => "emp"