# 11. Write a Python program to extract year, month and date from an URL.

import re 

s = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

x = re.findall("[0-9]+", s)

if len(x) > 0:
    print("Year:", x[0])
    print("Month:", x[1])
    print("Date:", x[2])
else:
    print("No date found!")