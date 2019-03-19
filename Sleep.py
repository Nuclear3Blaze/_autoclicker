import win32api as win,pyautogui as py,time as t,pygame as p
import keyboard as key
from __init__ import*
p.init()
clock = p.time.Clock()
def sleep(num_press):
    waiting = True
    timer = 2*50
    while waiting:
        if key.is_pressed("escape"):
            print("skipping user...")
            return 1
        clock.tick(fps)
        if win.GetCursorPos()[0] <= 100 or win.GetCursorPos()[0] >= 700:
            print("Resetting because cursor moved.")
            return 2
        timer -= 1
        if timer <= 0:
            waiting = False
    return 0
