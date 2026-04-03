# mini-projects/calculator.py

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose +, -, *, /: ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")