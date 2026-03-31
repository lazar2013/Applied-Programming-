# 7. Write a Python program to remove leading zeros from an IP address.
# Test: "216.08.094.196"

import re
s = input("Enter an IP address to remove '0's: ")
result = re.sub('0+([1-9])', '\\1', s)
print(result)