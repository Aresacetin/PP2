# Break and else in while loop
i = 4
while i < 10:
    if i == 6:
        break
    print(i)
    i += 1
else:
    # Will be executed if loop ended without break command
    print("Else block")
