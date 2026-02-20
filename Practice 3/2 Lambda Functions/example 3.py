# filter function is used with another function that returns boolean to filter some data from iterables

# removes odd numbers and keeps even numbers
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(lambda x: x % 2 == 0, a))
print(a)

# Removes composite numbers and keeps primes, it is not very efficient for many numbers but it works :)
a = list(range(1, 100))
a = list(filter(lambda x: x > 1 and not [i for i in range(2, int(x ** 0.5) + 1) if x % i == 0], a))
print(a)

