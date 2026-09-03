'''
get_first_and_last.py
Lists Exercise 1: Create and Access a List
Create a function named get_first_and_last that accepts a list and returns a tuple containing:
(first item, last item)
'''
def get_first_and_last(mylist):
    outlist = []
    if len(mylist) == 0:
        return outlist # blank list
    list_count = len(mylist)
    list_index = 0
    for _ in mylist:
        if list_index == 0:                   
            outlist.append(mylist[list_index])
        elif list_index == list_count - 1:
            outlist.append(mylist[list_index])
        list_index += 1
    return outlist


print(get_first_and_last(["red", "green", "blue"]))
# ("red", "blue")

print(get_first_and_last([10, 20, 30, 40]))
# (10, 40)

print(get_first_and_last(["only"]))
# ("only", "only")

print(get_first_and_last([]))