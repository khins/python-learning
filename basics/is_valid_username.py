'''
is_valid_username.py
Exercise 15: Validate a Username
Write is_valid_username(username) that returns True only when:
It is between 5 and 15 characters long.
It starts with a letter.
It contains only letters, digits, and underscores.
It does not start or end with an underscore.
It does not contain two underscores in a row.
Surrounding whitespace makes the username invalid; do not strip it.

'''
def is_valid_username(user_name):
    if len(user_name) < 5 or len(user_name) > 15:
        return False

    if "__" in user_name:
        return False
    if user_name.startswith('_') or user_name.endswith('_'):
        return False
    # is between 5 and 15 characters long.       
    has_proper_length = False
    if user_name != user_name.strip():
        return False  # Surrounding whitespace
    if len(user_name) >= 5 and len(user_name) <= 15:
        has_proper_length = True
    #starts with a letter
    has_first_letter = user_name[0].isalpha()
    #contains only letters, digits, and underscores
    has_ldu = False

    without_underscores = user_name.replace("_", "")
    has_ldu = without_underscores.isalnum()

    return (has_proper_length and
            has_first_letter and
            has_ldu 
            )
        


print(is_valid_username("python_user"))  # True
print(is_valid_username("Python123"))     # True
print(is_valid_username("1python"))       # False
print(is_valid_username("_python"))       # False
print(is_valid_username("python_"))      # False
print(is_valid_username("py__user"))     # False
print(is_valid_username("py-user"))     # False
print(is_valid_username(" abcde"))        # False
print(is_valid_username("abc"))           # False
print(is_valid_username("")) 