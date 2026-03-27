import re
s = input()
p = r".*\d{3}.*"
print(re.findall(p,s,re.I))