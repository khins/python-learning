'''
Exercise 6: Validate a Simple Product Code
Write a function that returns True when a product code:
Starts with "PROD-", ignoring capitalization.
Ends with exactly four numeric characters.

'''
def is_valid_code(product_code):
    if len(product_code[5:]) > 4:
        return False
    if product_code.lower().startswith('prod-'):
        if product_code[5:9].isdigit():
            num = product_code[5:9]
            if len(num) == 4:
                return True
        else:
            return False
    else:
        return  False

print(is_valid_code("PROD-1234"))  # True
print(is_valid_code("prod-5678"))  # True
print(is_valid_code("ITEM-1234"))  # False
print(is_valid_code("PROD-12AB"))  # False
print(is_valid_code("PROD-12345")) # False