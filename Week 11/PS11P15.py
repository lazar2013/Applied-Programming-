# 15. Write a Python program to remove multiple spaces from a string.
# Test: 
# 'Python      Exercises'

import re

s = input("Enter a string to remove multiple spaces: ")

result = re.sub(" +", " ", s)

print("Result:", result)