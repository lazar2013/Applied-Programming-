# 13. Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Test: 'Python Exercises, PHP exercises.'

import re 
s = "Python Exercises, PHP exercises."

result = re.sub("[ ,.]", ":", s)
print("Result:", result)
