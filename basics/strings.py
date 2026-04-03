# 03_strings.py

name = "Kevin"

print("Hello " + name)
print(f"Hello {name}")  # modern way, using f-strings

# String methods
text = "python is fun"

print(text.upper())
print(text.capitalize())
print(text.replace("fun", "awesome"))

# Length
print("Length:", len(text))

# Indexing
print("First letter:", text[0])
print("Last letter:", text[-1])

# 04_input_output.py

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old.")

age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# for loops
for i in range(5):  
    print(f"Iteration {i + 1}")

# while loops
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))