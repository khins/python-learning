'''
format_messy_name.py
Exercise 8: Format a Messy Name
Write a function named format_name that converts:
"   aDA    loVELAce   "

Requirements:
Remove surrounding whitespace.
Handle any number of spaces between the names.
Give each word an uppercase first letter and lowercase remaining letters.
Return the formatted name.
Try solving it without a loop.
'''
def format_name(name):
    words = name.strip().lower().split()
   
    return " ".join(words).title()
        
    
    
print(format_name("   aDA    loVELAce   "))