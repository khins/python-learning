'''
parse_email.py
Exercise 10: Parse an Email Address
Write a function named parse_email that accepts:
"  Ada.Lovelace@Example.COM  "
and returns:
("ada.lovelace", "example.com")
Requirements:
Remove surrounding whitespace.
Convert the address to lowercase.
Separate it at the @ character.
Return the username and domain as a tuple.
Assume the input contains exactly one @.
Do not use a loop.
'''
def parse_email(email):
    temp = email.strip().lower().split("@")
    return tuple(temp)

print(parse_email("  Ada.Lovelace@Example.COM  "))