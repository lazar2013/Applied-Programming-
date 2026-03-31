# 6. Write a Python program that matches a word containing 'z'.
# Test: 
# "The quick brown fox jumps over the lazy dog."
# "Python Exercises."

import re
s = input("Enter a string to search for a word containing the letter 'z':")

if re.search('[a-zA-Z]*z[a-zA-Z]*', s):
    print("Match!")
else:
    print("No Match! None of the words contain the letter 'z'")