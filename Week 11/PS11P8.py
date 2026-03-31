# 8. Write a Python program to search for literal strings within a string.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'

import re 

# Sample text
s = "The quick brown fox jumps over the lazy dog."

# Search for each word and print.
for word in ['fox', 'dog', 'horse']:
    if re.search(word, s):
        print("Found: ", word)
    else: 
        print("Not found: ", word)