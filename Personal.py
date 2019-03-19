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
import keyboard as key,os as o,numpy as np,cv2
import PIL
class Clicker:
    def __init__(self):
        p.init()
        self.precooldown = 3
        self.cooldown = 2
        self.fps = 60
        ##    Personal use Only!    x,y = 408,292
        ##    Public use Only!      x,y = 410,339
        self.x,self.y = 420,290
        self.xcoords2 = [561,607,680,734,788]
        self.ycoords2 = [210,216,215,205,215]
        self.colours = [(128,123,78),(115,53,41),(115,95,65),(123,86,86),(65,107,115)]
        self.clock = p.time.Clock()
        self.num_press = "1"
##        self.file_locations = ["C:/Users/27funkj/Desktop/img/berries00.png","C:/Users/27funkj/Desktop/img/berries01.png","C:/Users/27funkj/Desktop/img/berries02.png","C:/Users/27funkj/Desktop/img/berries03.png","C:/Users/27funkj/Desktop/img/berries04.png",
##                               ""]
        self.Starter()
    def Quit(self):
        p.quit()
        quit()
    def Starter(self):
        input("Press enter to begin...")
        self.users = 1
        self.fields = []
        self.run_clicker()
    def get_pixel_colour(self,x,y):
        return PIL.ImageGrab.grab().load()[x,y]
    def run_clicker(self):
        self.num_on = 1
        ##    t.sleep(precooldown)
        self.presleep()
        while True:
            num_clicks = 0
            self.key_changed = False
            py.press(self.num_press,pause=.2)
            self.click(45)
            ##    t.sleep(cooldown)
            self.sleep()
            py.press("d",pause=.2)
            t.sleep(.5)
            if self.num_press == "1":
                if self.get_pixel_colour(self.xcoords2[1],self.ycoords2[1]) == self.colours[1] or self.get_pixel_colour(self.xcoords2[1],self.ycoords2[1]-20) == self.colours[1]:
                    self.users += 1
                    self.fields.append(self.num_on)
                    self.run_clicker()
            elif self.num_press == "2":
                if self.get_pixel_colour(self.xcoords2[2],self.ycoords2[2]) == self.colours[2] or self.get_pixel_colour(self.xcoords2[2],self.ycoords2[2]-20) == self.colours[2]:
                    self.users += 1
                    self.fields.append(self.num_on)
                    self.run_clicker()
            elif self.num_press == "3":
                if self.get_pixel_colour(self.xcoords2[3],self.ycoords2[3]) == self.colours[3] or self.get_pixel_colour(self.xcoords2[3],self.ycoords2[3]-20) == self.colours[3]:
                    self.users += 1
                    self.fields.append(self.num_on)
                    self.run_clicker()
            elif self.num_press == "4":
                if self.get_pixel_colour(self.xcoords2[4],self.ycoords2[4]) == self.colours[4] or self.get_pixel_colour(self.xcoords2[4],self.ycoords2[4]-20) == self.colours[4]:
                    self.users += 1
                    self.fields.append(self.num_on)
                    self.run_clicker()
            elif self.num_press == "5":
                if self.get_pixel_colour(self.xcoords2[0],self.ycoords2[0]) == self.colours[0] or self.get_pixel_colour(self.xcoords2[0],self.ycoords2[0]-20) == self.colours[0]:
                    self.users += 1
                    self.fields.append(self.num_on)
                    self.run_clicker()
            py.scroll(-400)
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
    def click(self,times):
        if key.is_pressed("escape"):
            print("skipping user...")
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
        py.click(self.x,self.y,clicks=times)
clicker = Clicker()
##      py.press("1")
##      py.press("right")
