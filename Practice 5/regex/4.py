# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
s = input()
p = r"[A-Z][a-z]+"
r = re.search(p, s)
try:
    print(r.group(0))
except AttributeError:
    print("No match")

