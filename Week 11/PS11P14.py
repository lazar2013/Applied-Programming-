# 14. Write a Python program to find all words starting with 'a' or 'e' in a given string.
# Test: 
# "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then 
# added to the ArrayList and the ArrayList is trimmed accordingly."

import re 
s = input("Enter a phrase to filter all words that start with an 'a' or an 'e': ")

x = re.findall(r"\b[aeAE][a-zA-Z]*", s)

if len(x) > 0:
    print("Found words that start with an 'a' or an 'e':", x)
else: 
    print("Nothing found!")