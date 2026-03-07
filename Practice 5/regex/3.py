# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
s = input()
p = r"[a-z]+(_[a-z]+)+"
r = re.search(p, s)
try:
    print(r.group(0))
except AttributeError:
    print("No match")

