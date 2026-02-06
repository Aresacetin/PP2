# Count consonant amount in string
word = "Pythonic"
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char in vowels:
        continue
    count += 1
    print(f"Consonant: {char}")
print(count)
