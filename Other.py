"""
    This is an autoclicker. It will move the mouse position and click a certain spot
    on screen until interrupted by the user.

    This autoclicker scrolls the currently open window once ever 50 clicks, to get rid of
    this functionality press Ctrl and f, type in "WHEEL" andpress enter. It will highlight
    a piece of code. Place a hash symbol at the start of the line to stop the program from
    executing it (note hash symbol looks like this: #) the code will turn red.
    
    This autoclicker also presses various buttons for ease of access on a certain website.
    If you do not want the key presses to happen press Ctrl and f, type in "py.press" and
    press enter. It will highlight a piece of code. Place a hash symbol at the start of the
    line to stop the program from executing it (note hash symbol looks like this: #) the
    code will turn red. To find the next "py.press" you will need to click somewhere after
    the first one then do the steps again.

    To change where the mouse is clicking press Ctrl and f, type in "self.x" and press enter.
    It will highlight a piece of code. Go to the numbers after the equals sign, these are the
    coordinates at which the mouse will be clicked. Change these to wherever you need to be
    clicked.
"""
import win32api as win,win32con as con,time as t,sys as s,pygame as p,pyautogui as py
import keyboard as key, os as o
##o.system(command)
class Clicker:
    def __init__(self):
        p.init()
        self.precooldown = 3
        self.cooldown = 2
        self.fps = 60
        ##    Personal use Only!    x,y = 408,292
        ##    Public use Only!      x,y = 410,339
        self.xcoords = [420,658,272,565,272,565,272,565,369]
        self.ycoords = [365,92,447,447,549,549,651,651,697]
        self.xcoords2 = [561,607,680,734,788]
        self.ycoords2 = [255,262,260,250,260]
        self.x,self.y = 420,345
        self.clock = p.time.Clock()
        self.num_press = "1"
        self.Starter()
##    def key_pressed(self,num=None):
##        if num != None:
##            self.num_press = str(num)
##            self.key_changed = True
##            print(self.num_press)
    def Starter(self):
        input("Press enter to begin...")
        self.run_clicker()
##    def party_click(self):
##        if self.pre:
##            win.mouse_event(con.MOUSEEVENTF_WHEEL,0,0,1000,0)
##            t.sleep(.5)
##            win.SetCursorPos((self.xcoords[1],self.ycoords[1]))
##            win.mouse_event(con.MOUSEEVENTF_LEFTDOWN,self.xcoords[1],self.ycoords[1],0,0)
##            win.mouse_event(con.MOUSEEVENTF_LEFTUP,self.xcoords[1],self.ycoords[1],0,0)
##            t.sleep(3)
##            for i in range(2,8,1):
##                win.SetCursorPos((self.xcoords[i],self.ycoords[i]))
##                win.mouse_event(con.MOUSEEVENTF_LEFTDOWN,self.xcoords[i],self.ycoords[i],0,0)
##                win.mouse_event(con.MOUSEEVENTF_LEFTUP,self.xcoords[i],self.ycoords[i],0,0)
##            t.sleep(1.5)
##            win.SetCursorPos((self.xcoords[7],self.ycoords[7]))
##            win.mouse_event(con.MOUSEEVENTF_LEFTDOWN,self.xcoords[7],self.ycoords[7],0,0)
##            win.mouse_event(con.MOUSEEVENTF_LEFTUP,self.xcoords[7],self.ycoords[7],0,0)
##            t.sleep(1.5)
##            win.SetCursorPos((self.xcoords[8],self.ycoords[8]))
##            win.mouse_event(con.MOUSEEVENTF_LEFTDOWN,self.xcoords[8],self.ycoords[8],0,0)
##            win.mouse_event(con.MOUSEEVENTF_LEFTUP,self.xcoords[8],self.ycoords[8],0,0)
##            t.sleep(1.5)
##            win.SetCursorPos((self.xcoords[8],self.ycoords[8]))
##            win.mouse_event(con.MOUSEEVENTF_LEFTDOWN,self.xcoords[8],self.ycoords[8],0,0)
##            win.mouse_event(con.MOUSEEVENTF_LEFTUP,self.xcoords[8],self.ycoords[8],0,0)
##            t.sleep(3)
##            win.mouse_event(con.MOUSEEVENTF_WHEEL,0,0,-1000,0)
##            self.pre = False
##            win.SetCursorPos((500,500))
    def run_clicker(self):
##        o.system("C:/Users/27funkj/Desktop/doneDetector00.exe")
##        o.system("C:/Users/27funkj/Desktop/doneDetector01.exe")
##        o.system("C:/Users/27funkj/Desktop/doneDetector02.exe")
##        o.system("C:/Users/27funkj/Desktop/doneDetector03.exe")
##        o.system("C:/Users/27funkj/Desktop/doneDetector04.exe")
        self.num_on = 1
        ##    t.sleep(precooldown)
        self.presleep()
##        self.pre = True
        while True:
            num_clicks = 0
            self.key_changed = False
            py.press(self.num_press,pause=.2)
            while num_clicks < 50:
                num_clicks += 1
                self.click()
                if self.num_on == 2:
                    win.SetCursorPos((408,422))
                    win.mouse_event(con.MOUSEEVENTF_LEFTDOWN,408,422,0,0)
                    win.mouse_event(con.MOUSEEVENTF_LEFTUP,408,422,0,0)
                    t.sleep(.2)
                    win.SetCursorPos((413,457))
                    win.mouse_event(con.MOUSEEVENTF_LEFTDOWN,413,457,0,0)
                    win.mouse_event(con.MOUSEEVENTF_LEFTUP,413,457,0,0)
                    self.num_on += 1
                    t.sleep(1)
            ##    t.sleep(cooldown)
            self.sleep()
            py.press("d",pause=.2)
##            if self.num_on%10 == 0:
##                if self.num_press == "1":
##                    py.press("left control+alt+a")
##                    win.SetCursorPos((self.xcoords2[0],self.ycoords2[0]))
##                elif self.num_press == "2":
##                    py.press("left control+alt+b")
##                    win.SetCursorPos((self.xcoords2[1],self.ycoords2[1]))
##                elif self.num_press == "3":
##                    py.press("left control+alt+c")
##                    win.SetCursorPos((self.xcoords2[2],self.ycoords2[2]))
##                elif self.num_press == "4":
##                    py.press("left control+alt+d")
##                    win.SetCursorPos((self.xcoords2[3],self.ycoords2[3]))
##                else:
##                    py.press("left control+alt+e")
##                    win.SetCursorPos((self.xcoords2[4],self.ycoords2[4]))
##                try:
##                    with open("done00.txt","r") as f:
##                        o.system('del "C:/Users/27funkj/Desktop/done00.txt"')
##                        self.party_click()
##                except:
##                    pass
            win.mouse_event(con.MOUSEEVENTF_WHEEL,0,0,-400,0)
            self.num_on += 1
    def presleep(self):
        waiting = True
        timer = self.precooldown*50
        while waiting:
            self.clock.tick(self.fps)
            timer -= 1
            if timer <= 0:
                waiting = False
    def sleep(self):
        waiting = True
        timer = self.cooldown*50
        while waiting:
            if not self.key_changed:
                if key.is_pressed("1"):
                    self.num_press = ("1")
                    self.key_changed = True
                elif key.is_pressed("2"):
                    self.num_press = ("2")
                    self.key_changed = True
                elif key.is_pressed("3"):
                    self.num_press = ("3")
                    self.key_changed = True
                elif key.is_pressed("4"):
                    self.num_press = ("4")
                    self.key_changed = True
                elif key.is_pressed("5"):
                    self.num_press = ("5")
                    self.key_changed = True
            self.clock.tick(self.fps)
            if win.GetCursorPos()[0] <= 100 or win.GetCursorPos()[0] >= 700:
                print("Resetting because cursor moved.")
                self.Starter()
            timer -= 1
            if timer <= 0:
                waiting = False
    def click(self):
        if key.is_pressed("1"):
            self.num_press = ("1")
            self.key_changed = True
        elif key.is_pressed("2"):
            self.num_press = ("2")
            self.key_changed = True
        elif key.is_pressed("3"):
            self.num_press = ("3")
            self.key_changed = True
        elif key.is_pressed("4"):
            self.num_press = ("4")
            self.key_changed = True
        elif key.is_pressed("5"):
            self.num_press = ("5")
            self.key_changed = True
        win.SetCursorPos((self.x,self.y))
        win.mouse_event(con.MOUSEEVENTF_LEFTDOWN,self.x,self.y,0,0)
        win.mouse_event(con.MOUSEEVENTF_LEFTUP,self.x,self.y,0,0)
clicker = Clicker()
##      py.press("1")
##      py.press("right")
