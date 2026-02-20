class MyClass:
    # Class variables
    value1 = 5
    value_str = "wasd"
    custom_variable_i_guess = [1, 2, 3]

my_object = MyClass()

print(my_object.value1)
print(my_object.value_str)
print(my_object.custom_variable_i_guess)

my_object.new_var = "wow!"

print(my_object.new_var)

second_object = MyClass()

my_object.child = second_object

print(my_object.child.value1)

