# Summing only positive terms
a = [10, -5, 20, -1, 30]
s = 0
for i in a:
    if i < 0:
        continue  # Skip the rest of the code for this number
    s += i
print(s)
