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


