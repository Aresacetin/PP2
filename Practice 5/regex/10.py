# Write a Python program to convert a given camel case string to snake case
import re
s = input()
p = r"(\w)([A-Z])"
a = lambda x: x.group(1) + "_" + x.group(2).lower()
r = re.sub(p, a, s)
print(r)

