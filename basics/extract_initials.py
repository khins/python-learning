'''
Write a function that takes a full name, removes surrounding spaces, and prints the person’s initials in uppercase.
Example input:
"   ada lovelace   "
'''

def extract_name(name):
    name_temp = name.split()
    first_initial = name_temp[0][0]
    second_initial = name_temp[1][0]

    return first_initial.capitalize() + second_initial.capitalize()
    
print(f'{extract_name("   ada lovelace   ")}')