'''
format_product_entry.py
Step #3 Exercise: Parse, Validate, and Format
Write a function named format_product_entry that processes input like:
"  keyboard:49  "
and returns:
Keyboard costs $49
Rules:
Remove surrounding whitespace.
Split the input at :.
The product must contain only letters.
The price must contain only digits.
If either part is invalid, return "Invalid entry".
Format the product using an appropriate casing method.
Assume the input contains exactly one colon.

Requirements:
There must be exactly one colon.
Allow surrounding whitespace around the complete input and each part.
Product names must contain only letters.
Prices must contain only digits.
Invalid input must not cause an exception.
Keep your else if that makes the control flow clearer.
'''
def format_product_entry(product):
    if product.count(":") != 1:
        return "Invalid entry"  
           
    product_name, price = product.split(":")
    product_name = product_name.strip()
    price = price.strip()
 
    if product_name.isalpha() and price.isdigit():
        return f'{product_name.capitalize()} costs ${price}'
    else:
        return "Invalid entry"
        

print(format_product_entry("keyboard:49"))     # "Keyboard costs $49"
print(format_product_entry(" keyboard : 49 "))  # "Keyboard costs $49"
print(format_product_entry(""))
print(format_product_entry("keyboard:49:10"))
print(format_product_entry(":49"))
print(format_product_entry("keyboard:"))
print(format_product_entry("key-board:49"))
print(format_product_entry("keyboard"))