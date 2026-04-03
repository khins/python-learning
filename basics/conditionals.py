# 05_conditionals.py

age = 20

print("Checking age...")

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# Multiple conditions
score = 85

print("\nChecking score...")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

print("\n--- User Check ---")

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You can enter")
else:
    print("Too young")

number = 7
print("\nChecking if number is even or odd...")
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# temp check
temperature = 30
print("\nChecking temperature...")
if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's warm outside.")
else:
    print("It's cold outside.")

# password check
password = input("\nEnter your password: ")
if password == "secret123":
    print("Access granted.")
else:
    print("Access denied.")