# sum_of_lengths.py
# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
def sum_of_lengths(values):
    total = 0
    for word in values:
        for w in word:
            total += 1

    return total



# EXAMPLES
print(sum_of_lengths(["Hello", "Bob"])) #                => 8
print(sum_of_lengths(["Nonsense"])) #                    => 8
print(sum_of_lengths(["Nonsense", "or", "confidence"])) # => 20


# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# EXAMPLES
def product(values):
    total = 1
    for num in values:
    
        total *= num
    return total



print(product([1, 2, 3])) #    => 6
print(product([4, 5, 6, 7])) #  => 840
print(product([10])) #           => 10