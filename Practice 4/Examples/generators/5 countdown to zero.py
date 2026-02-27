def countdown(N):
    for i in range(N, -1, -1):
        yield i

for i in countdown(int(input())):
    print(i)


