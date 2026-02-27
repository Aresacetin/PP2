# Write a Python program to calculate the area of regular polygon.
import math
n = float(input("Input number of slides: "))
a = float(input("Input the length of a side: "))
print(f"The area of the polygon: {n*pow(a, 2)/(4*math.tan(math.pi/n)):.0f}")
