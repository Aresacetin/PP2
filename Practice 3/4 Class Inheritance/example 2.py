# defining parent class
class PClass:

    def pmethod(self):
        print("Method from PClass")

# Inherit everythin from parent and change nothing
class CClass1(PClass):
    pass

# Inherit from parent and overriding some methods
class CClass2(PClass):    
    # overriding parent class method
    def pmethod(self):
        print("Method override, now it is from CClass2")

p = PClass()
p.pmethod()
c1 = CClass1()
c1.pmethod()
c2 = CClass2()
c2.pmethod()

