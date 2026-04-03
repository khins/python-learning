# 09_file_handling.py
# 🔹 File Handling
import os
with open("example.txt", "w") as file:
    content = file.write("testing file handling in Python.")

with open("example.txt", "r") as file:
    content = file.read()
print(f"Content of example.txt: {content}")

file_path = os.path.join(os.path.dirname(__file__), "example.txt")

with open(file_path, "r") as file:
    content = file.read()

print(f"Content of example.txt using os.path: {content}")