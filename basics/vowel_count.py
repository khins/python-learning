# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")        => 3
# vowel_count("helicopter")    => 4
# vowel_count("ssh")           => 0
def vowel_count(word):
    return len(word)
    
print(f'estate is : {vowel_count("estate")}')
print(f'helicopter is : {vowel_count("helicopter")}')
print(f'ssh is : {vowel_count("ssh")}')