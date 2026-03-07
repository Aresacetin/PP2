# Write a Python program to insert spaces between words starting with capital letters
import re
s = input()
p = r"(\w)(?=[A-Z])"
a = r"\1 "
r = re.sub(p, a, s)
print(r)

