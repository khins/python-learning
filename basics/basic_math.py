# basic_math.py

# Basic numbers
a = 10
b = 3

print("a =", a)
print("b =", b)

print("\n--- Basic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)  # returns float

print("\n--- More Operations ---")
print("Floor Division:", a // b)  # removes decimals
print("Modulus (remainder):", a % b)
print("Exponent:", a ** b)

print("\n--- Order of Operations ---")
result = (a + b) * 2
print("(a + b) * 2 =", result)

print("\n--- Incrementing ---")
a = a + 1
print("a after increment:", a)

# shorthand
a += 5
print("a after += 5:", a)

a = 7
b = 2
print("\n--- More Math Functions ---")
number = 10 

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")