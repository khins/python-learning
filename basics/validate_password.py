'''
validate_password.py
Exercise 13: Validate a Password
Write a function named is_valid_password that returns True only when a password:
Has at least 8 characters.
Contains no spaces.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Contains at least one digit.
You may use string methods, conditionals, and a loop
'''
def is_valid_password(password_val):
    # Contains no spaces.
    
    contains_cap = False   
    contains_digit = False
    contains_lower = False
    has_proper_length = False
    contains_space = False

    if len(password_val) >= 8:
        has_proper_length = True

    for character in password_val:
        
        if character.isupper(): # Contains at least one uppercase letter.
            contains_cap = True
            
        if character.islower(): 
            contains_lower = True # Contains at least one lowercase letter.
            
        if character.isdigit():  # Contains at least one digit.
            contains_digit = True

        if character == " ":
            contains_space = True    

    return (
        contains_cap
        and contains_lower
        and contains_digit
        and has_proper_length
        and not contains_space
    )
    

print(is_valid_password("Python123"))  # True
print(is_valid_password("python123"))  # False
print(is_valid_password("PYTHON123"))  # False
print(is_valid_password("PythonABC"))  # False
print(is_valid_password("Py 12345"))   # False
print(is_valid_password("Py123"))      # False