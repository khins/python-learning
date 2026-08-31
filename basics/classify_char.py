'''
classify_char.py
Control Flow Exercise 4: Classify Characters
Write count_character_types(text) that examines every character and returns a tuple containing:
(letter_count, digit_count, whitespace_count, other_count)
Requirements:
Use a for loop.
Use four accumulator variables.
Use if/elif/else so each character enters only one category.

'''
def count_character_types(string):
    # return (letter_count, digit_count, whitespace_count, other_count)
    letter_count = 0
    digit_count = 0
    whitespace_count = 0
    other_count = 0
    for letter in string:
        if letter.isalpha():
            letter_count += 1
        elif letter.isdigit():
            digit_count += 1
        elif letter.isspace():
            whitespace_count += 1
        else:
            other_count += 1
    return (letter_count, digit_count, whitespace_count, other_count)


print(count_character_types("Hello 123!"))   # (5, 3, 1, 1)
print(count_character_types("Python\n3.14"))  # (6, 3, 1, 1)
print(count_character_types("   "))           # (0, 0, 3, 0)
print(count_character_types(""))              # (0, 0, 0, 0)
print(count_character_types("@#$"))           # (0, 0, 0, 3)