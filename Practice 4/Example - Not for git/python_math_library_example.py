# Write a Python program to convert degree to radian.
import math
a = float(input("Input degree: "))/180
pi=22/7
# pi=math.pi
print(f"Output radian: {a*pi:6f}")

# Write a Python program to calculate the area of a trapezoid.
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
print(f"Expected Output: {h*(a+b)/2}")

# Write a Python program to calculate the area of regular polygon.
import math
n = float(input("Input number of slides: "))
a = float(input("Input the length of a side: "))
print(f"The area of the polygon: {n*pow(a, 2)/(4*math.tan(math.pi/n)):.0f}")

# Write a Python program to calculate the area of a parallelogram.
l = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
print(f"Expected Output: {l*h:.1f}")