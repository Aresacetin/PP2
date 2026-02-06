# Finding position of item in list
a = ["abc", "wasd", "lmnop", "qwerty", "fast"]
for i in range(len(a)):
    if a[i] == "lmnop":
        print(f"lmnop at position {i + 1}")
        break

