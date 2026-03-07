# Write a Python program to split a string at uppercase letters.
import re
s = input()
p = r"[A-Z]"
r = re.split(p, s)
print(r)

