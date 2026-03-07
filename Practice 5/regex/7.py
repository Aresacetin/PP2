# Write a python program to convert snake case string to camel case string.
import re
s = input()
p = r"_([a-zA-Z0-9])"
r = re.sub(p, lambda match: match.group(1).upper(), s)
print(r)

