# Generator that yields numbers:
a = int(input())
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_up_to(a):
    print(num)


# Generator that yield squares of numbers:
a = int(input())
def square_up_to(n):
    counter = 1
    count = 1
    while counter <= n:
        yield count
        counter += 1
        count = counter * counter
print("\n".join(map(str,square_up_to(a))))

# Gererator that yield even numbers:
a = int(input())
def even_up_to(n):
    count = 0
    while count <=n:
        yield count
        count += 2
first = True
for num in even_up_to(a):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False

# Generator thar yield divisiblity numbers by 3 and 4 (12):
a = int(input())
def divisiblity_by_12(n):
    count = 0
    while count <= n:
        yield count 
        count += 12
for num in divisiblity_by_12(a):
    print(num , end=" ")

# Generator that yield number squares from A to B:
a,b = map(int, input().split())
def square_a_to_b(n,k):
    count = n
    counter = n
    while counter <= k:
        count = counter * counter
        yield count
        counter += 1
for num in square_a_to_b(a,b):
    print(num)

# Generator that yield numbers from n to 0:
a = int(input())
def countdown(n):
    count = n
    while count>=0:
        yield count
        count -= 1
for num in countdown(a):
    print(num)

# Generator that yields fibonacchi sequence up to n:
a = int(input())
def fibonacchi_sequence(n):
    f1=0
    f2=1
    counter = 0
    while counter < n:
        yield f1
        f1,f2=f2,f2+f1
        counter += 1
first = True
for num in fibonacchi_sequence(a):
    if not first:
        print("," , end="")
    print(num , end="")
    first=False