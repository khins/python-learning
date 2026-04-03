# 07_functions.py
# Function definition   
def greet(name):
    """Greets the person with their name."""
    return f"Hello, {name}!"

# Function call
print(greet("Alice"))

# Add parameters with Return values
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

print(add(5, 3))

# Default parameters
def greet(name="Guest"):
    """Greets the person with their name or 'Guest' if no name is provided."""
    return f"Hello, {name}!"

print(greet())
print(greet("Bob"))

# Multiple returns (tuple)
def math_ops(a, b):
    """Returns the sum, difference, product, and quotient of a and b."""
    return a + b, a - b, a * b, a / b
sum_, diff, prod, quot = math_ops(10, 5)
print(f"Sum: {sum_}, Difference: {diff}, Product: {prod}, Quotient: {quot}")

# Combine everything
def check_even(num):
    """Checks if a number is even or odd."""
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."

print(check_even(4))
print(check_even(7))

# Square function
def square(x):
    """Returns the square of x."""
    return x ** 2
print(square(5))

# Max of two numbers    
def max_of_two(a, b):
    """Returns the maximum of a and b."""
    if a > b:
        return a
    else:
        return b
print("Maximum of 10 and 20 is:", max_of_two(10, 20))

# Temperature converter
def celsius_to_fahrenheit(c):
    """Converts Celsius to Fahrenheit."""
    return (c * 9/5) + 32
print("25°C is equal to", celsius_to_fahrenheit(25), "°F")

# Even filter   
def filter_even(numbers):
    """Returns a list of even numbers from the given list."""
    return [num for num in numbers if num % 2 == 0]
print(filter_even([1, 2, 3, 4, 5, 6]))

