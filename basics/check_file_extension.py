'''
Exercise 5: Check a File Extension
Write a function that checks whether a filename ends with .py, ignoring capitalization.
'''

def is_python_file(name):
    return name.lower().endswith('.py')

print(is_python_file("exercise.py"))    # True
print(is_python_file("PROGRAM.PY"))     # True
print(is_python_file("notes.txt"))      # False