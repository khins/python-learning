print("-- Loops -- ")
# For loop
print("\n-- For Loop --")
for i in range(5):
    print(f"Iteration {i}")

# now for a custom range
print("\n-- Custom Range --")
for i in range(1, 10, 2):
    print(f"Odd number: {i}")

# while loop
print("\n-- While Loop --")
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Looping through a list
print("\n-- Looping through a List --")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")    

# break and continue
print("\n-- Break and Continue --")
for i in range(10):
    if i == 5:
        print("Breaking the loop at 5")
        break
    if i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue
    print(f"Processing number: {i}")

    # combineing loops and conditionals
print("\n-- Combining Loops and Conditionals --")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# challenge 1 - sum of first n numbers
print("\n-- Challenge: Sum of First n Numbers --")
n = 10
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"The sum of the first {n} numbers is: {total_sum}")      

# challenge 2 - countdown from n
print("\n-- Challenge: Countdown from n --")
n = 10
print(f"Countdown from {n}:")
for i in range(n, 0, -1):
    print(i)
print("Liftoff!")

# challenge 3 - multiplication table
print("\n-- Challenge: Multiplication Table --")
num = 5
print(f"Multiplication Table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# List comprehension
print("\n-- List Comprehension --")
numbers = [1, 2, 3, 4, 5]
print(numbers)

# list comprehension with logic
# 🧠 Pattern with condition
# [expression for item in iterable if condition]
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Transform data
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Work with strings
names = ["alice", "bob", "charlie"]
greetings = [f"Hello, {name.capitalize()}!" for name in names]
print(greetings)

#Add if/else inside comprehension
numbers = [1, 2, 3, 4, 5]   
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Number labels: {labels}")

# condition at the end (filter)
[i for i in range(10) if i % 2 == 0]
print(f"Even numbers from 0 to 9: {[i for i in range(10) if i % 2 == 0]}")

# double numbers
doubled = [x * 2 for x in numbers]
print(f"Doubled numbers: {doubled}")

# Filter long words
words = ["short", "medium", "longer", "lengthy"]
long_words = [word for word in words if len(word) > 5]
print(f"Long words: {long_words}")

# Squares of even numbers
squared_evens = [x**2 for x in numbers if x % 2 == 0]
print(f"Squares of even numbers: {squared_evens}")

