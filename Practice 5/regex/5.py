# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
s = input()
p = r"^a.*b$"
r = re.search(p, s)
try:
    print(r.group(0))
except AttributeError:
    print("No match")

