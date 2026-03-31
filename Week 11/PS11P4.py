# 4. Write a Python program to find sequences of lowercase letters joined by an underscore.
# Test: 
# "aab_cbbbc"
# "aab_Abbbc"
# "Aaab_abbbc"

import re 
s = input("Enter a string to search for lowercase letters joined by an underscore:")
x = re.findall('[a-z]+_[a-z]+', s)
if len(x) > 0:
    print("Match found:", x)
else: 
    print("No Match!")