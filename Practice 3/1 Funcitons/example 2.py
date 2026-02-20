# Functions arguments


# x is argument of function plus_five and we need to pass it when we call the function
def plus_five(x):
    print(x + 5)

plus_five(2)

number = 10
plus_five(number)



# return keyword will return some value from function that we can use

def is_even(num):
    return num % 2 == 0

res = is_even(4)
print(res)

res = is_even(123)
print(res)



# default and keyword arguments

def strip_str(s, rstrip=True, lstrip=True):
    if rstrip:
        s = s.rstrip()
    if lstrip:
        s = s.lstrip()
    return s

print(strip_str("   wasd     "))
print(strip_str("   wasd     ", lstrip=False))
print(strip_str("   wasd     ", rstrip=False))
print(strip_str("   wasd     ", lstrip=False, rstrip=False))




# *args for unknown amount of arguments, passes as a tuple

def max_even(*args):
    return max(list(filter(lambda x: x % 2, args)))

print(max_even(1, 2, 3, 4, 123, 999))




# **kwargs for unknown amount of keyword arguments, passes as a dictionary


def calculate_position(**kwargs):
    return (kwargs["screen_size_x"] * kwargs["pos_x"], kwargs["screen_size_y"] * kwargs["pos_y"])


print(calculate_position(screen_size_x=1920, screen_size_y=1080, pos_x=0.5, pos_y=0.5))


