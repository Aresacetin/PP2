
# defining parent class
class PClass:

    def pmethod(self):
        print("Method from PClass")

# Inherit everythin from parent and add own methods
class CClass1(PClass):

    def cmethod(self):
        print("Method from CClass")
    
    def pcmethod(self):
        print("PC method")
        self.pmethod()
        self.cmethod()


p = PClass()
p.pmethod()
try:
    p.cmethod()
except:
    print("no cmethod in pclass")
c1 = CClass1()
c1.pmethod()
c1.cmethod()
c1.pcmethod()
