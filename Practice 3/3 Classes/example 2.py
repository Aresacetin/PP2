class MyClass:
    money = 0
    
    # Functions inside classes are called methods, first argument of method is always an object reference
    # following arguments work same as in normal functions
    # Usually this object reference is called self
    # methods can return values just like as normal function
    def deposit(self, amount):
        if amount > 0:
            self.money += amount
        return self.money

    def withdraw(self, amount):
        if amount > 0:
            self.money -= amount
        return self.money
    
    # to create new variable inside class we need to create in self
    def create_new_class_var(self):
        self.new = 50

obj = MyClass()
print(obj.money)
m = obj.deposit(100)
print(m, obj.money)
r = obj.withdraw(23)
print(r, obj.money)

try:
    print(obj.new)
except:
    print("No obj.new")

obj.create_new_class_var()
print(f"obj.new is {obj.new}")

