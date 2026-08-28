'''
classify_text.py
Step #2 Exercise: Classify Input
Write a function named classify_text that returns:
"letters" if the input contains only letters
"letters and numbers" if it contains only letters and numbers
"whitespace" if it contains only whitespace
"other" for anything else, including punctuation
'''
def classify_text(text_val):
   # check for input "letters" if the input contains only letters
   
    if text_val.isalpha():
        return "letters"
    elif text_val.isalnum():
        return "letters and numbers"
    elif text_val.isspace():
        return "whitespace"
    else:
        return "other"


print(classify_text("Python"))     # "letters"
print(classify_text("Python3"))    # "letters and numbers"
print(classify_text("   "))        # "whitespace"
print(classify_text("Hello!"))     # "other"