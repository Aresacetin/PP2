
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, GPA):
        # Calling parent's init method with super
        super().__init__(name)
        self.GPA = GPA

    def display(self):
        print(f"Student: {self.name}, GPA: {self.GPA}")

n, g = "Di", 4.1
s = Student(n, g)
s.display()

