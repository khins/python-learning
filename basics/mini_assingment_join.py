'''
mini_assignment_join.py
words = ["mary", "anne", "smith"]
Use the .join() string method—without a loop—to produce:
mary anne smith
'''

def joiner(name):
    return " ".join(name)
    
print(joiner(["mary", "anne", "smith"]))