import win32api as win,pyautogui as py,time as t,pygame as p
from __init__ import*
p.init()
clock = p.time.Clock()
def presleep():
    waiting = True
    timer = 3*50
    while waiting:
        clock.tick(fps)
        timer -= 1
        if timer <= 0:
            waiting = False
