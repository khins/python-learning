'''
truthy_exercise.py
# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string "even".
# If the integer is odd, the function should return the string "odd".
#
# even_or_odd(2)    => "even"
# even_or_odd(0)    => "even"
# even_or_odd(13)   => "odd"
# even_or_odd(9)    => "odd"


# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value ____ is ____"
# where the first space is the argument and the second space
# is either 'truthy' or 'falsy'. See the sample invocations below.
#
# truthy_or_falsy(0)       => "The value 0 is falsy"
# truthy_or_falsy(5)       => "The value 5 is truthy"
# truthy_or_falsy("Hello") => "The value Hello is truthy"
# truthy_or_falsy("")      => "The value  is falsy"
'''
def even_or_odd(num):
    if num % 2:
        return "even"
    return "odd"

def truthy_or_falsy(word):
    if bool(word):
        return f'The value of {word} is truthy'
    return f'The value of {word} if falsy'


print(even_or_odd(2)) #    => "even"
print(even_or_odd(0)) #   => "even"
print(even_or_odd(13)) #   => "odd"
print(even_or_odd(9)) #    => "odd"
print(truthy_or_falsy(0)) # => "The value 0 is falsy"
print(truthy_or_falsy(5)) # => "The value 5 is truthy"
print(truthy_or_falsy("Hello")) # => "The value Hello is truthy")
print(truthy_or_falsy("")) #     => "The value  is falsy"