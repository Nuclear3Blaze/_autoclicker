import pyautogui as py,time as t
def reload(page=None):
    if page != None:
        py.click(415,50)
        t.sleep(3)
        py.typewrite(page,pause=.2)
        t.sleep(3)
        py.press("return",pause=.2)
    else:
        py.press("f5")
        t.sleep(3)
        py.press("f5")
