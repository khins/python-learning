'''
collect_until_stop.py
Control Flow Exercise 7: Stop with break
Write collect_until_stop(words) that returns a new list containing words encountered before "stop".
Requirements:
Use a for loop.
Use break when "stop" is encountered.
Treat "STOP", "Stop", and other capitalization variants as "stop".
Do not include the stop word in the returned list.
If no stop word exists, return every word.
Do not modify the original list.

'''
def collect_until_stop(words: list[str]):
    mylist = []
    for word in words:
        if word.lower() == "stop":
            break
        mylist.append(word)

    return mylist

print(collect_until_stop(["red", "blue", "stop", "green"]))  
# ["red", "blue"]

print(collect_until_stop(["one", "STOP", "two"]))            
# ["one"]

print(collect_until_stop(["apple", "banana"]))               
# ["apple", "banana"]

print(collect_until_stop(["Stop"]))                          
# []

print(collect_until_stop([]))                                
# []

# Correct. for handles both the end of the list and an empty list automatically, while break exits early when the stop word appears.