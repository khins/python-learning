'''
countdown.py
Control Flow Exercise 6: Build a Countdown
Write make_countdown(start) that returns a list counting down from start to 1.
Requirements:
Use a while loop.
Create an empty list before the loop.
Use .append() to add the current number to the list.
Decrease the counter by 1 each iteration.
Return an empty list when start is 0 or negative.
Do not use range().

'''
def make_countdown(start):
    mylist = []
    current_value = start
    
    while current_value > 0:
        mylist.append(current_value)
        current_value -= 1
    return mylist



print(make_countdown(5))   # [5, 4, 3, 2, 1]
print(make_countdown(1))   # [1]
print(make_countdown(0))   # []
print(make_countdown(-3))  # []

# Correct. This is a clean while loop with one changing state variable