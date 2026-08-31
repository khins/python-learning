'''
factorial.py
# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number.
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kind of loops.
# Instead, utilize recursion. Your function MUST call itself.
# See sample inputs and return values below
#
# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120
Use a while loop.
Start the result accumulator at 1.
Return 1 when number is 0, because 0! = 1.
Return "Invalid input" for negative numbers.
Do not use math.factorial().
Assume the input is always an integer.
'''
def factorial(number):
    
    if number < 0:
        return "Invalid input"
    result = 1 # accumulator
    counter = 1

    while counter <= number:
        result *= counter
        counter += 1 

    return result


print(factorial(1))  # 1
print(factorial(2))  # 2
print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120

# Correct. This is a clean iterative factorial implementation.