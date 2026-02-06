# if statements can be nested
a = 15
if a > 1:
    print(f"{a} is greater than 1")
    if a > 10:
        print(f"{a} is greater than 10")
        if a > 100:
            print(f"{a} is greater than 100")
        print("end of 100 check")
    print("end of 10 check")
print("end of 1 check")
