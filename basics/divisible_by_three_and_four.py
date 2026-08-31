'''
divisible_by_three_and_four
# Define a divisible_by_three_and_four function that accepts a number as its argument.
# It should return True if the number is evenly divisible by both 3 and 4.
# It should return False otherwise.
#
# divisible_by_three_and_four(3)   => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True


# Declare a string_theory function that accepts a string as an argument.
# It should return True if the string has more than 3 characters
# and starts with a capital "S". It should return False otherwise.
#
# string_theory("Sansa")  => True
# string_theory("Story")  => True
# string_theory("See")    => False
# string_theory("Fable")  => False
'''
def divisible_by_three_and_four(num):
    if num % 3 == 0 and num % 4 == 0:
        return True
    return False


def string_theory(word):
    return len(word) > 3 and word[0] == "S"

print(divisible_by_three_and_four(3))   # False
print(divisible_by_three_and_four(4))   # False
print(divisible_by_three_and_four(12))  # True
print(divisible_by_three_and_four(18))  # False
print(divisible_by_three_and_four(24))  # True 
print(string_theory("Sansa"))  # True
print(string_theory("Story"))  # True
print(string_theory("See"))    # False
print(string_theory("Fable"))  # False