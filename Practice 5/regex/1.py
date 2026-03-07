# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
s = input()
p = r"ab*"
r = re.search(p, s)
try:
    print(r.group(0))
except AttributeError:
    print("No match")
