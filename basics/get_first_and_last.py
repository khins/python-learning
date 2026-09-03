'''
get_first_and_last.py
Lists Exercise 1: Create and Access a List
Create a function named get_first_and_last that accepts a list and returns a tuple containing:
(first item, last item)
Requirements:
Use list indexing.
Do not use a loop.
Do not modify the original list.
Use a negative index to access the final item.
'''
def get_first_and_last(mylist):
    
    if len(mylist) == 0:
        return () # blank list

    first_item = mylist[0]
    last_item = mylist[-1]
    return (first_item,last_item)


print(get_first_and_last(["red", "green", "blue"]))
# ("red", "blue")

print(get_first_and_last([10, 20, 30, 40]))
# (10, 40)

print(get_first_and_last(["only"]))
# ("only", "only")

print(get_first_and_last([]))