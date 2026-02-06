# Finding first non-positive integer in list
a = [15, 23, 0, -12, 24, -1, 6]
for i in a:
    if i <= 0:
        print(i)
        break
