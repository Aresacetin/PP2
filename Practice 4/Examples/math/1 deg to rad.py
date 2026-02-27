from math import pi

def deg_to_rad(deg):
    return deg / 180 * pi

deg = int(input("Input degree: "))
print(f"Output radian: {deg_to_rad(deg):.9f}")

