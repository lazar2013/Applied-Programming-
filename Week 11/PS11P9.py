# 9. Write a Python program to search for a literal string in a string and also find the location within the original string 
# where the pattern occurs.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'

import re 

s = "The quick brown fox jumps over the lazy dog."

x = re.search("fox", s)

if x:
    print("Found:", x.group())
    print("Location:", x.start())
else:
    print("Not found!")