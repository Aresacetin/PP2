# Advanced inheritance
from math import sin, pi
class Parallelogramm:
    def __init__(self, width, height, angle):
        self.width = width
        self.height = height
        self.angle = angle # in degrees

    def area(self):
        return self.width * self.height * sin(self.angle/180 * pi)

# Rectangle is a parallelogramm with 90 degree angle
# so we just need to lock angle to 90 degrees
class Rectangle(Parallelogramm):
    def __init__(self, width, height):
        super().__init__(width, height, 90)

# Square is a rectangle with equal side lenghts 
# so we just need to set width and height to same value
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

p = Parallelogramm(6, 2, 45)
r = Rectangle(5, 8)
s = Square(7)
print(p.area())
print(r.area())
print(s.area())

