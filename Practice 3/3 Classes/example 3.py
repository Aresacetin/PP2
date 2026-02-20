class MyClass:
    # init method is called on object creation, and arguments passed 
    # on object creation will be passed into init method
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

obj = MyClass("Asus Zehpyrus G14", 2023)
print(obj.name, obj.birth_year)

