
def div_by_twelve(N):
    for i in range(0, N + 1, 12):
        yield i

n = int(input())
for i in div_by_twelve(n):
    print(i, end=" ")

