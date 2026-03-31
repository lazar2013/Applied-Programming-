# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# Test: 
# "ABCDEFabcdef123450"
# "*&%@#!}{"

import re 
s = input("Enter a string to see if it contains only letters and numbers:")
# Search for letters A-Z and a-z as well as numbers only. 
if re.search('[a-zA-Z0-9]+', s):
    print("Match!")
else:
    print("No match!")