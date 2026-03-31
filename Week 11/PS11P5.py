# 5. Write a Python program that matches a word at the beginning of a string.
# Test:
# "The quick brown fox jumps over the lazy dog."
# The quick brown fox jumps over the lazy dog.

import re
s = input("Enter a string to check for a word at the beginning:")

# Search for a word at the beginning. 
if re.search('^[a-zA-Z]+', s):
    print("Match! String starts with a word!")
else:
    print("No Match! String does not start with a word.")