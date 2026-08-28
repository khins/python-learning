'''
mask_phone_number.py
Exercise 9: Mask a Phone Number
Write a function named mask_phone_number that converts:
"555-123-4567"

Preserve the final four characters.
Replace every earlier digit with *.
Preserve the hyphens.
Return the masked number.
For this exercise, assume the input always follows ###-###-####.
Try to use string slicing and .replace() rather than a loop.
'''
def mask_phone(phone_number):
    last_four = phone_number[-4:]
    return f'***-***-{last_four}'

print(mask_phone("555-123-4567")) #***-***-4567
print(mask_phone("123-456-7123"))

