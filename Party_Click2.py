import win32api as win,pyautogui as py,time as t
from __init__ import*
def party_click():
    py.scroll(2000)
    t.sleep(.5)
    py.click(xcoords3[9],ycoords3[9])
    t.sleep(6)
    py.scroll(100)
    t.sleep(0)
    py.scroll(-130)
    t.sleep(1.5)
    for i in range(2,8,1):
        py.click(xcoords3[i],ycoords3[i])
    t.sleep(1.5)
    py.click(xcoords3[7],ycoords3[7])
    t.sleep(1.5)
    py.click(xcoords3[8],ycoords3[8])
    t.sleep(1.5)
    py.click(xcoords3[8],ycoords3[8])
    t.sleep(3)
    py.scroll(-2000)
    pre = False
    win.SetCursorPos((500,500))
