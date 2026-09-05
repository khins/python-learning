# Define a smallest_number function that accepts a list of numbers.
# It should return the smallest value in the list.
#
# EXAMPLES
def smallest_number(values):
    smallest_num = values[0]

    for num in values:
        if num < smallest_num:
            smallest_num = num

    return smallest_num

print(smallest_number([1, 2, 3])) #    => 1
print(smallest_number([3, 2, 1])) #    => 1
print(smallest_number([4, 5, 4])) #   => 4
print(smallest_number([-3, -2, -1])) # => -3


# Define a concatenate function that accepts a list of strings.
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# EXAMPLES
def concatenate(values):
    string = ""
    for word in values:
        if len(word) > 2:
            string += word
    return string

print(concatenate(["abc", "def", "ghi"])) #          => "abcdefghi"
print(concatenate(["abc", "de", "fghi", "ic"])) #    => "abcfghi"
print(concatenate(["ab", "cd", "ef", "gh"])) #       => ""


# Define a super_sum function that accepts a list of strings.
# The function should sum the index positions of the first occurrence of the letter "s" in each
#
# Not every word is guaranteed to have an "s".
# Don't use "sum" as a variable name as it's a built-in keyword.

# Define a super_sum function that accepts a list of strings.
# The function should sum the index positions of
# the first occurrence of the letter "s" in each word.
#
# Not every word is guaranteed to have an "s".
# Don't use "sum" as a variable name as it's a built-in keyword.
#
# EXAMPLES
def super_sum(values):
    total = 0
    if len(values) == 0:
        return 0
    for word in values:
        if "s" in word:
            index = word.index("s")
            total += index
    return total



print(super_sum([])) #                                     => 0
print(super_sum(["mustache"])) #                            => 2
print(super_sum(["mustache", "greatest"])) #                => 8
print(super_sum(["mustache", "pessimist"])) #               => 4
print(super_sum(["mustache", "greatest", "almost"])) #      => 12