# if-elif-else statements can be nested
in_air = False
is_jump_button_pressed = True
auto_jump_enabled = True
is_in_front_of_wall = False
if not in_air:
    if is_jump_button_pressed:
        print("Jump!")
    elif auto_jump_enabled and is_in_front_of_wall:
        print("Jump!")
    else:
        print("On ground")
