# split_in_two.py
# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element
# to the end of the list.
#
# If the number is odd, return the list elements from
# index 0 (inclusive) to 2 (exclusive)
#
# EXAMPLE:
values = ["a", "b", "c", "d", "e", "f"]
def split_in_two(mylist,num):
    outlist = []
    if num % 2 == 0: # if even
        return mylist[2:]

    return mylist[0:2]



print(split_in_two(values, 3)) #    => ["a", "b"]
print(split_in_two(values, 4)) #    => ["c", "d", "e", "f"]
print(split_in_two(values, 1)) #    => ["a", "b"]
print(split_in_two(values, 10)) #   => ["c", "d", "e", "f"]