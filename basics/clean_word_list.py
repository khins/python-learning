'''
clean_word_list.py
Control Flow Exercise 8: Skip with continue
Write clean_word_list(words) that:
Removes surrounding whitespace from each word.
Skips empty or whitespace-only items.
Converts retained words to lowercase.
Returns a new list.
Does not modify the original list.
Requirements:
Use a for loop.
Use continue to skip unusable items.
Use .strip() and .lower().
'''
def clean_word_list(words):
    mylist = []
    for w in words:
        clean_word = w.strip().lower()
        if len(clean_word) == 0:
           continue     
           
        mylist.append(clean_word) 
    return mylist



print(clean_word_list(["  Apple ", "", " BANANA", "   ", "Cherry  "]))
# ["apple", "banana", "cherry"]

print(clean_word_list(["PYTHON", " Code "]))
# ["python", "code"]

print(clean_word_list(["", " ", "\t", "\n"]))
# []

print(clean_word_list([]))
# []

# Correct. This version uses continue appropriately and avoids unnecessary nesting.