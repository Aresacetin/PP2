
def sqaures(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a, b = map(int, input().split())
for i in sqaures(a, b):
    print(i)

