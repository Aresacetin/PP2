
def sqaures(N):
    for i in range(1, N + 1):
        yield i ** 2

for i in sqaures(int(input())):
    print(i)

