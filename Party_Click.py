import win32api as win,pyautogui as py,time as t,Get_Pixel_Colour as gtp
from __init__ import*
def party_click():
    py.scroll(2000)
    t.sleep(.5)
    py.click(xcoords[1],ycoords[1])
    t.sleep(6)
    if gtp.get_pixel_colour(xcoords2[5],ycoords2[5]) == colours[5] or gtp.get_pixel_colour(xcoords2[5],ycoords2[5]-20) == colours[5]:
        return
    py.scroll(100)
    t.sleep(0)
    py.scroll(-220)
    t.sleep(1.5)
    for i in range(2,8,1):
        py.click(xcoords[i],ycoords[i])
    t.sleep(1.5)
    py.click(xcoords[7],ycoords[7])
    t.sleep(1.5)
    py.click(xcoords[8],ycoords[8])
    t.sleep(1.5)
    py.click(xcoords[8],ycoords[8])
    t.sleep(3)
    py.scroll(-2000)
    pre = False
    win.SetCursorPos((500,500))
