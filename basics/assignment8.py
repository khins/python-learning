'''
Questions for this assignment
How can you check if the string "and" is found in the string "commando"?

What number does the index start counting from?

What will the code below evaluate to?

"commando"[3:7]

What will the code below evaluate to?

"monroeville"[6:]

What will the code below evaluate to?

"destiny"[:4]

What is the difference between ​\n​ and ​\t​?

What function calculates the number of characters in a string?

What is the technical word that means “to combine strings together”?

What will the code below evaluate to?

"november"[6]

What will the code below evaluate to?

"misfortune"[10]
'''

def word_slice(word):
    return word[3:7]
    
print(word_slice("commando"))

def word_slice2(word):
    return word[6:]
    
print(word_slice2("monroeville"))

def word_slice3(word):
    return word[:4]
    
print(word_slice3("destiny"))