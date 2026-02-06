# string comparison, works lexicographically for smaller and greater than operators
a = "abc"
b = "xyz"
c = "abc"
d = "acd"
print(a > b)  # False
print(a == c) # True
print(a != c) # False
print(d < b)  # True
print(a >= c) # True
print(a > c)  # False
