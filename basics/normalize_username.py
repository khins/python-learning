'''
Starts with this string:username = "   PyThOn_Learner   "

Removes the spaces at both ends.
Converts every character to lowercase.
Prints the result.
'''

def normal_username(name):
    return name.strip().lower()
    
print(f'{normal_username("   PyThOn_Learner   ")}')