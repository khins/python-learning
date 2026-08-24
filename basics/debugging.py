
def find_largest(numbers):
    # Initialize the largest number to the first element in the list
    largest = numbers[0]
    
    for number in numbers:
        if number > largest:
            largest = number
    return largest
    
result = find_largest([12, 7, 25, 4])
print(f"Largest: {result}")
print(find_largest([-12, -7, -25, -4]))