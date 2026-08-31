'''
while_loop.py
Control Flow Exercise 5: Introduce while
Write sum_to(limit) that returns the sum of every integer from 1 through limit.
Examples:
sum_to(5) → 1 + 2 + 3 + 4 + 5 → 15
Requirements:
Use a while loop.
Start a counter at 1.
Start a total accumulator at 0.
Add the counter to the total during each iteration.
Increase the counter during each iteration.
Return 0 when limit is 0 or negative.
Do not use sum() or range().
'''
def sum_to(limit):
    count = 1
    total = 0
    while count <= limit:
        # Add the counter to the total during each iteration.
        # Increase the counter during each iteration.
        total += count 
        count += 1
        
    return total


print(sum_to(5))   # 15
print(sum_to(1))   # 1
print(sum_to(10))  # 55
print(sum_to(0))   # 0
print(sum_to(-3))  # 0