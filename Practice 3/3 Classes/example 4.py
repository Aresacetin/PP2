class MyClass:

    # class variable is shared across every object and class and can be changed without object creation
    cls = "cls_value1"

    def __init__(self):
        # object variable is individual to every object
        self.obj = "obj_value1"
    
    # class method can be called without object creation
    # require @staticmethod decorator before defining method
    # does not contain self argument
    @staticmethod
    def cls_print():
        print("print from cls_print")

    # object method can be called from object
    def obj_print(self):
        print("print from obj_print")

obj1 = MyClass()
obj2 = MyClass()
print(obj1.cls, "|", obj2.cls)
MyClass.cls = "cls_value3"
print(obj1.cls, "|", obj2.cls)

obj1.obj = "obj changed in obj1"
print(obj1.obj, "|", obj2.obj)

MyClass.cls_print()
obj1.obj_print()
