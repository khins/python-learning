'''
Exercise 4: Replace Banned Words
Write a function that replaces every occurrence of "bad" with "***".

Expected result:
This is a *** example with another *** word.
'''

def censor_text(original_string,text_to_find, replacement_text):

    return original_string.replace(text_to_find,replacement_text)


print(censor_text("This is a bad example with another bad word.", "bad", "***"))