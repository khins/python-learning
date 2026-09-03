'''
lists_examples.py
'''
# Create an empty list and assign it to the variable "empty".
empty = []

# Create a list with a single Boolean - True - and
# assign it to the variable "active".
active = [True]

# Create a list with 5 integers of your choice and
# assign it to the variable "favorite_numbers".
favorite_numbers = [7,9,3,5,1]

# Create a list with 3 strings - "red", "green", "blue"
# and assign it to the variable "colors".
colors = ["red","green","blue"]

# Declare an is_long function that accepts a single list as an argument.
# It should return True if the list has more than 5 elements, and False otherwise
def is_long(arg):
    return len(arg) > 5

print(is_long([1,6,8]))
print(is_long([7,6,5,4,3,2,1]))

