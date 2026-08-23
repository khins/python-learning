'''
numbers = [10, 20, 30, 40, 50]
Write a loop that:
Prints each number
Calculates the sum of all the numbers
Prints the total after the loop finishes
'''
numbers = [10, 20, 30, 40, 50]
sum_numbers = 0    

for number in numbers:
    print(number)
    sum_numbers += number
    
print(f'Total = {sum_numbers}')