# 10. Write a Python program to replace whitespaces with an underscore and vice versa.
# Test: “Regular Expressions” and “Code_Examples”

import re

s = input("Enter a string to replace whitespaces with underscores or vice versa: ")

# Replace whitespaces with underscores.
result1 = re.sub(' ', '_', s)

# Replace underscores with whitespaces.
result2 = re.sub('_', ' ', s)

print("Whitespaces replaced with underscores:", result1)
print("Underscores replaced with whitespaces:", result2)