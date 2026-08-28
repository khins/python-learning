''' learning-python-string-methods
Exercise 7: Create a URL Slug
Write a function that converts a title into a URL-friendly slug.
First hint: keep your current approach, but remove the unwanted
character from the end of temp2 before returning it. Which string
method removes specified characters from only the right side of a
string?
One design observation: your loop creates a separator after
 every word and then repairs the final result. Python has a 
 string method specifically for placing a separator between a 
 collection of strings. We’ll encounter that method soon.
'''
def create_slug(url):
    temp = url.strip().split()
    temp2 = ""
    for t in temp:
        t = t.lower() + "-"
        temp2 += t
    return temp2.rstrip("-")
    

print(create_slug("   Learning Python String Methods   "))  # learning-python-string-methods