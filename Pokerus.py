import win32api as win,win32con as con,time as t,pygame as p,pyautogui as py
import keyboard as key,os as o,numpy as np,cv2
import PIL
import Party_Click as pc,Party_Click2 as pc2,Field_Click as fc,Presleep as ps,Reload as r
class Clicker:
    def __init__(self):
        self.Starter()
    def Starter(self):
        self.run_clicker()
    def Quit(self):
        p.quit()
        quit()
        input()
    def run_clicker(self):
        self.num_on = 1
        field_code = -3
        self.last_time = -3
        new_fc = -3
        self.start_time = t.time()
        ps.presleep()
        self.pre = True
        while True:
            time = t.localtime()
            if time[4]%15 == 0 and time[4] != self.last_time:
                self.last_time = time[4]
                print("moving to new pokerus host.")
                new_fc = -3
                field_code = -3
                self.num_on = 1
                r.reload()
                t.sleep(6)
##            if t.time()-self.start_time >= 7200:
##                print("active for: "+str(self.start_time)+" seconds")
##                print("resetting page due to being active for over 2 hours.")
##                new_fc = -3
##                field_code = -3
##                self.start_time = t.time()
##                r.reload()
            if field_code == 2 or field_code == 5 or field_code == 4:
                if new_fc != 0:
                    self.num_on = 1
                    pc2.party_click()
                new_fc = fc.field_click(self.num_on)
                if new_fc != 0:
                    field_code = -1
            else:
                if field_code != 0:
                    self.num_on = 1
                    pc.party_click()
                field_code = fc.field_click(self.num_on)
            if field_code == 6 or new_fc == 6:
                self.Quit()
            self.num_on += 1
clicker = Clicker()
