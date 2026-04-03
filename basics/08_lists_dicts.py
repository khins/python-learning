# 08_lists_dicts.py
# Lists
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers[0])
print(numbers[-1])  # last element
numbers.append(6)
print("After appending 6:", numbers)
numbers.remove(3)
print("After removing 3:", numbers)
print("Length of numbers:", len(numbers))

#🔹 Loop through list
print("\n-- Looping through list --")
for num in numbers:
    print(num * 2)  

# 🔹 Dictionaries (key-value pairs)
print("\n-- Dictionaries --")
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Person:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# 🔹 Modify dictionary
person["age"] = 31
print("After updating age:", person)
person["city"] = "Cincinnati"
print("After updating city:", person)

# 🔹 Loop through dictionary
print("\n-- Looping through dictionary --")
for key, value in person.items():
    print(f"{key}: {value}")

# 🔹 List of dictionaries
print("\n-- List of dictionaries --")
users = [
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28}
]
for user in users:
    print(f"{user['name']} is {user['age']} years old.")

# 🧪 Mini challenges
print("\n-- Mini Challenges --")
# #Filter users under 18
# Create list of names only
# Add a new user to list

print("\n-- Filter users under 30 --")
for user in users:
    if user["age"] < 30:
        print(f"{user['name']} is under 30.")

print("\n-- List of names only --")
names = [user["name"] for user in users]
print("Names:", names)

print("\n-- Add a new user --")
new_user = {"name": "Eve", "age": 22}
users.append(new_user)
print("After adding new user:", users)


