# Skipping elements with small length
a = ["abc" "abcdefg", "This is a long string", "shrt"]
i = -1
while i < len(a) - 1:
    i += 1
    if len(a[i]) < 5:
        continue
    print(a[i])
