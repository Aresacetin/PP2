# function documentation with docstrings

def calculate_position(**kwargs):
    """
    Calculates absolute position from relative position and screen size
    
    Arguments:
    screen_size_x - screen width in pixels, 
    screen_size_y - screen height in pixels, 
    pos_x - relative position on screen from 0 to 1 by width
    pos_y - relative position on screen from 0 to 1 by height
    """
    return (kwargs["screen_size_x"] * kwargs["pos_x"], kwargs["screen_size_y"] * kwargs["pos_y"])

print(calculate_position.__doc__)

