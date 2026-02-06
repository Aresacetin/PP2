# Summing even numbers
s = 0
for i in range(10):
    if i % 2 == 1:
        continue
    s += i
print(s)
