# Count consonant amount in string
word = "Pythonic"
vowels = "aeiouAEIOU"
index = 0
count = 0
while index < len(word):
    char = word[index]
    index += 1
    if char in vowels:
        continue
    count += 1
    print(f"Consonant: {char}")
print(count)
