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
        self.xcoords = [420,658,272,565,272,565,272,565,369]
        self.ycoords = [365,92,447,447,549,549,651,651,697]
        self.xcoords2 = [561,607,680,734,788]
        self.ycoords2 = [255,261,260,250,260]
        self.colours = [(128,123,78),(115,53,41),(115,95,65),(123,86,86),(65,107,115)]
        self.x,self.y = 420,345
        self.clock = p.time.Clock()
        self.num_press = "5"
        self.Starter()
##    def key_pressed(self,num=None):
##        if num != None:
##            self.num_press = str(num)
##            self.key_changed = True
##            print(self.num_press)
    def Starter(self):
        input("Press enter to begin...")
        self.start_time = t.time()
        self.users = 1
        self.fields = []
        self.run_clicker()
    def party_click(self):
        if self.pre:
            py.scroll(2000)
            t.sleep(.5)
            py.click(self.xcoords[1],self.ycoords[1])
            t.sleep(3)
            py.scroll(-100)
            t.sleep(.5)
            for i in range(2,8,1):
                py.click(self.xcoords[i],self.ycoords[i])
            t.sleep(1.5)
            py.click(self.xcoords[7],self.ycoords[7])
            t.sleep(1.5)
            py.click(self.xcoords[8],self.ycoords[8])
            t.sleep(1.5)
            py.click(self.xcoords[8],self.ycoords[8])
            t.sleep(3)
            py.scroll(-2000)
            self.pre = False
            win.SetCursorPos((500,500))
##    def get_area_colour(self,x,y,w,h):
##        List = []
##        for i in range(y,y+h):
##            for k in range(x,x+w):
##                List.append(PIL.ImageGrab.grab().load()[x,y])
##        return List
    def reload(self):
        py.press("f5")
        t.sleep(1)
        py.press("f5")
    def get_pixel_colour(self,x,y):
        return PIL.ImageGrab.grab().load()[x,y]
    def run_clicker(self):
        self.num_on = 1
        ##    t.sleep(precooldown)
        self.presleep()
        self.pre = True
        while True:
            self.party_click()
            self.num_clicks = 0
            self.key_changed = False
            py.press(self.num_press,pause=.2)
            self.click(45)
            if self.num_on == 2:
                if self.users == 15:
                    py.click(408,432)
                    t.sleep(.2)
                    py.click(413,467,clicks=2)
                else:
                    py.click(408,427)
                    t.sleep(.2)
                    py.click(413,462,clicks=2)
                self.num_on *= -1
                t.sleep(1)
            ##    t.sleep(cooldown)
            self.num_on = abs(self.num_on)
            self.sleep()
            py.press("d",pause=.2)
            self.num_on += 1
            t.sleep(.5)
            if t.time()-self.start_time >= 7200:
                print("resetting page due to being active for over 2 hours.")
                self.reload()
                self.users += 1
                self.fields.append(self.num_on)
                self.run_clicker()
##            print(self.get_pixel_colour(self.xcoords2[1],self.ycoords2[1]),self.get_pixel_colour(self.xcoords2[1],self.ycoords2[1]+20))
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
            win.mouse_event(con.MOUSEEVENTF_WHEEL,0,0,-400,0)
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
            if key.is_pressed("escape"):
                print("skipping user...")
                self.run_clicker()
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
                self.num_clicks -= 50
                print("Clicked "+str(self.users)+" user(s), "+str(self.num_on+sum(self.fields))+
                      " 'fields' for a total of: "+str(sum(self.fields)*45+
                                                       6*self.users)+" clicks.")
                self.Starter()
            timer -= 1
            if timer <= 0:
                waiting = False
    def click(self,times):
        if key.is_pressed("escape"):
            print("skipping user...")
            self.num_clicks += 50
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
