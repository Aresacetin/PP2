
def even(N):
    for i in range(0, N + 1, 2):
        yield i

n = int(input())
for i in even(n):
    print(i, end="")
    if i != n and i != n - 1:
        print(",", end="")

