# 12. Write a Python program to find all words starting with 'a' or 'e' in a given string.
# Test: 
# "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added
# to the ArrayList and the ArrayList is trimmed accordingly."

import re

s = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

# Find all the words starting with an "a" or an "e."
x = re.findall(r"\b[aeAE][a-zA-Z]*", s)

if len(x) > 0:
    print("Words starting with an 'a' or an 'e':", x)
else:
    print("Nothing found!")