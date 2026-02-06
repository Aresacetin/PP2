# Finding first number that is divisible by 3 and 5
num = 1
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print(f"The first number divisible by 3 and 5 is: {num}")
        break
    num += 1
