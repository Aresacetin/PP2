# Passing list and other objects as arguments


# Passing list and other objects passes a reference to original object, 
# therefore, when we change object in function the original changes too
def add(x, item):
    if x is list:
        x.append(item)
    if x is set:
        x.add(item)
    if x is dict:
        x[item] = 1

my_list = [1, 2, 3]
add(my_list, "new_item")
print(my_list)

my_set = {1, 2, 3}
add(my_set, 10)
print(my_set)

my_dict = {"key": "value", "wasd": "wasdwasd"}
add(my_dict, "new_key_very_original_i_know")
print(my_dict)
