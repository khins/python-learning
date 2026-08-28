'''
detect_palindrome.py
Exercise 12: Detect a Palindrome
Write a function named is_palindrome that checks whether a phrase 
reads the same forward and backward after ignoring spaces and capitalization.
Requirements:
Remove all spaces.
Ignore capitalization.
Return a Boolean.
Do not use a loop.
Use string slicing to reverse the normalized text.
'''
def is_palindrome(words):
    # Remove all spaces.
    normalized = words.replace(" ", "").lower()
    reverse_words = normalized[::-1]
    
    return normalized == reverse_words



print(is_palindrome("Race car"))       # True
print(is_palindrome("Never odd or even"))  # True
print(is_palindrome("Python"))         # False