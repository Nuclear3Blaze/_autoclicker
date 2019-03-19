"""
    This module is used to click at a spot on the screen for a specified number of times.
    
"""

"""
    pyautogui is used spefically for the click part of the function.
    keyboard is used to detect if a key is pressed.
    values used from __init__:
                x
                y
    
"""
import pyautogui as py,keyboard as key
from __init__ import x,y

"""
    The click function requires times and num_press as parameters,
    times is the number of times to click,
    num_press is not directly used. It is just passed so it can be returned if it changes.
    
"""
def click(times,num_press):
    """
        The click function returns either 0 or 1 as well as num_press.
        1 is used as a sort of error code used to force a change of user.
        0 will just be ingored as that is what is expected in most cases.
        
    """
    if key.is_pressed("escape"):
        print("skipping user...")
        return 1,num_press
    if key.is_pressed("1"):
        num_press = ("1")
        key_changed = True
    elif key.is_pressed("2"):
        num_press = ("2")
        key_changed = True
    elif key.is_pressed("3"):
        num_press = ("3")
        key_changed = True
    elif key.is_pressed("4"):
        num_press = ("4")
        key_changed = True
    elif key.is_pressed("5"):
        num_press = ("5")
        key_changed = True
    py.click(x,y,clicks=times)
    return 0,num_press
