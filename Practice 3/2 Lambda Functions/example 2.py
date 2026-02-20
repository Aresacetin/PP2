# Map function with lambdas

# map function takes another function and applies it to every item of some iterable
# most frequent use is inputting list of numbers as integers and not numbers

nums = list(map(int, input().split()))
print(nums)

# Square every number inside list with lambda
nums = list(map(lambda x: x ** 2, nums))
print(nums)

# makes even numbers negative
nums = list(map(lambda x: -x if x % 2 == 0 else x, nums))
print(nums)

# Makes every number non-negative
nums = list(map(lambda x: abs(x), nums))
print(nums)

