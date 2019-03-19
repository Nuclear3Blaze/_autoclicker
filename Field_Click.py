"""
    This module is used to click a user's field.
    
"""

"""
    pyautogui is used for clicking places, scrolling the screen, and pressing buttons.
    time is used to control the flow of the program somewhat.
    Sleep is also used to control the flow of the program, however it allows other code to be
    run while it is used.
    Get_Pixel_Colour is used to get the colour of a pixel at a certain spot on the screen.
    Click is used to click at a certain spot on the screen.
    values used from __init__:
                colours
                xcoords2
                ycoords2
                num_press
    
"""
import pyautogui as py,time as t,Sleep as s
import Get_Pixel_Colour as gtp,Click as c
from __init__ import colours,xcoords2,ycoords2,num_press

"""
    This function requires num_on as a parameter.
    num_on is used to bypass the autclicker detection.
    
"""
def field_click(num_on):
    if gtp.get_pixel_colour(xcoords2[5],ycoords2[5]) == colours[5] or gtp.get_pixel_colour(xcoords2[5],ycoords2[5]-20) == colours[5]:
        return 4
    py.scroll(-1000)
    if num_on == 2:
        py.click(394,423)
        t.sleep(.2)
        py.click(402,461,clicks=2)
        t.sleep(1)
    if num_on == 1:
        t.sleep(1)
        if gtp.get_pixel_colour(815,468) == (0,0,0):
            print("no fields to click...")
            return 2
    py.press(num_press,pause=.2)
    c.click(45,num_press)
    sleep_code = s.sleep(num_press)
    if sleep_code == 1:
        return 5
    elif sleep_code == 2:
        return 6
    py.press("d",pause=.2)
    py.scroll(-400)
    t.sleep(.5)
    if num_press == "1":
        if gtp.get_pixel_colour(xcoords2[1],ycoords2[1]) == colours[1] or gtp.get_pixel_colour(xcoords2[1],ycoords2[1]-20) == colours[1]:
            return 4
    elif num_press == "2":
        if gtp.get_pixel_colour(xcoords2[2],ycoords2[2]) == colours[2] or gtp.get_pixel_colour(xcoords2[2],ycoords2[2]-20) == colours[2]:
            return 4
    elif num_press == "3":
        if gtp.get_pixel_colour(xcoords2[3],ycoords2[3]) == colours[3] or gtp.get_pixel_colour(xcoords2[3],ycoords2[3]-20) == colours[3]:
            return 4
    elif num_press == "4":
        if gtp.get_pixel_colour(xcoords2[4],ycoords2[4]) == colours[4] or gtp.get_pixel_colour(xcoords2[4],ycoords2[4]-20) == colours[4]:
            return 4
    else:
        if gtp.get_pixel_colour(xcoords2[0],ycoords2[0]) == colours[0] or gtp.get_pixel_colour(xcoords2[0],ycoords2[0]-20) == colours[0]:
            return 4
    py.scroll(-400)
    return 0
