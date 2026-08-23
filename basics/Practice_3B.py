'''
numbers = [12, -5, 8, -3, 20, -7]
Write one loop that:
Prints "Positive: 12" for each positive number
Prints "Negative: -5" for each negative number
Counts how many positive numbers there are
Counts how many negative numbers there are
Prints both counts after the loop
Do not use sum() or list comprehensions yet.
'''
numbers = [12, -5, 8, -3, 20, -7]
postive_num = 0
negative_num = 0

for number in numbers:
    if number > 0:
        postive_num += 1
        print(f'Positive: {number}')
    if number < 0:
        negative_num += 1
        print(f'Negative: {number}')
    
print(f'Count postive: {postive_num}')
print(f'Count negative: {negative_num}')