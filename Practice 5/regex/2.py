# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
s = input()
p = r"ab{2}b?"
r = re.search(p, s)
try:
    print(r.group(0))
except AttributeError:
    print("No match")

