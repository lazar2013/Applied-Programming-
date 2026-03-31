# 3. Write a Python program that matches a string that has an a followed by one or more b's.
# Test: 
# “ab”
# “abc”
# “a”
# “ab”
# “abb”

import re
s = input("Enter a string to check for 'a' followed by one or more 'b's:")
# Search for "a" followed by one or more b's.
if re.search('ab+', s):
    print("Match!")
else:
    print("No Match!")