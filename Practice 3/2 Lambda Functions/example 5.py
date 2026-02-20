# Lambda vs traditional functions
# traditional functions are taking more space than lambdas but 
# they can be divided into different parts and be more readable and understandable


# Finding primes with lambda
a = list(range(1, 100))
a = list(filter(lambda x: x > 1 and not [i for i in range(2, int(x ** 0.5) + 1) if x % i == 0], a))
print(a)



# Finding primes with traditional functions
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


def filter_primes(until=100):
    nums = tuple(range(1, until))
    res = []

    for x in nums:
        if is_prime(x):
            res.append(x)
    
    return res

print(filter_primes())
