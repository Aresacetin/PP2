# if-elif-else statement, indentation marks begining and ending of if block
# the first condition to be true will execute and rest are skipped
# else block will execute if all conditions are false
a = 10
if a > 30:
    print(f"{a} is bigger than 30")
elif a > 20:
    print(f"{a} is bigger than 20")
elif a > 10:
    print(f"{a} is bigger than 10")
elif a > 0:
    print(f"{a} is bigger than 0")
else:
    print(f"{a} is a negative number")
