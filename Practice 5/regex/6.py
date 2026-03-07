# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
s = input()
p = r"[ ,.]"
a = ":"
r = re.sub(p, a, s)
print(r)
