# Else block will run if loop did not end with break
a = [1, 2, 6, 0, 5]
for i in a:
    if i == 0:
        print("Error, Division by zero")
        break
    print(f"Reciprocal of {i} is {1/i}")
else:
    print("No error")
