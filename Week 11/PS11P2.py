# 2. Write a Python program that matches a string that has an a followed by zero or more b's.
# Test: 
# “ab”
# “abc”
# “a”
# “ab”
# “abb”

import re 
s = input("Enter a string to check for an 'a' followed by 0 or more 'b's:")
# Search for "a" followed by either 0 or more b's. 
if re.search("ab*", s):
    print("Match!")
else:
    print("No Match!")