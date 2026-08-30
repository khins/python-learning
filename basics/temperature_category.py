'''
temperature_category.py
Write a function named classify_temperature that accepts a temperature in degrees Fahrenheit and returns:
"Freezing" when the temperature is 32 or below
"Cold" when it is above 32 but below 60
"Comfortable" when it is from 60 through 79
"Hot" when it is 80 or above
Requirements:
Use if, elif, and else.
Return the category rather than printing inside the function.
Pay close attention to boundary values: 32, 60, 79, and 80.
'''
def classify_temperature(temp):
    if temp <= 32:
        return "Freezing"
    elif temp < 60:
        return "Cold"
    elif temp < 80:
        return "Comfortable"
    else:
        return "Hot"




print(classify_temperature(20))   # "Freezing"
print(classify_temperature(32))   # "Freezing"
print(classify_temperature(45))   # "Cold"
print(classify_temperature(60))   # "Comfortable"
print(classify_temperature(79))   # "Comfortable"
print(classify_temperature(80))   # "Hot"
print(classify_temperature(32.5))  # Expected: Cold
print(classify_temperature(59.5))  # Expected: Cold
print(classify_temperature(79.5))  # Expected: Comfortable