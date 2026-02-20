# Multiple inheritance
class A:
    def m(self):
        print("m of A called")
        
class B(A):
    def m(self):
        print("m of B called")
        super().m()

class C(A):
    def m(self):
        print("m of C called")
        super().m()

class D(B, C):
    def m(self):
        print("m of D called")
        super().m()

d = D()
d.m()
# Output follows MRO (D -> B -> C -> A)
