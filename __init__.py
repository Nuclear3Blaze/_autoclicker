"""
    This file contains many constants that other parts of the autoclicker use,
    as such it is not meant to be run by itself and is instead imported where it is needed.
    
"""

"""
   This value is used to control the speed that the Sleep and Pre_Sleep modules execute.
   Changing this may break the autoclicker, so do so with caution.
   
"""
fps = 60

"""
    These are the x and y coordinates on the screen that are used for two main purposes.
    They are for clicking at/moving to, or for checking the pixel at that coordinate.
    xcoords and ycoords are used in Party_Click to navigate to a page, then click a users
    party, finishing by navigating to the users field where the autoclicker does most of its
    clicking.
    
"""
xcoords = [420,1157,249,558,249,558,249,558,369,658]
ycoords = [365,218,367,367,504,504,650,650,720,92]
xcoords3 = [420,1157,249,558,249,558,249,558,369,658]
ycoords3 = [365,218,433,433,541,541,639,639,702,92]
xcoords2 = [563,607,681,733,788,797]
ycoords2 = [254,261,261,250,260,306]

"""
    These are various RGB colours that the program uses to determine if the autoclicker
    should switch to a new user because the current one has no more fields to click.
    
"""
colours = [(128,123,78),(115,53,41),(115,95,65),(123,86,86),(65,107,115),
           (214,123,255)]

"""
    These are the main x and y values where the autoclicker will be clicking.
    x2 and y2 are used to bypass the wbesites built in autoclicker detection.
    x3 and y3 are used to make sure the autoclicker does not click your own user when they
    have pokerus.
    
"""
x,y = 420,335
x2,y2 = 526,347
x3,y3 = 824,426

"""
    These values are not used. They would theoretically be used to determine what number to
    press once I get around to finding out how to detect if a specific object is on the
    screen.
    
"""
width,height = 298,79

"""
    This is used to keep track of the current time, and in turn refresh the webpage every 15
    minutes.
    
"""
last_time = -1


"""
    This value dictates what number will be pressed before clicking, possible values range
    from 1 to 5 including both.
    
"""
num_press = "5"
