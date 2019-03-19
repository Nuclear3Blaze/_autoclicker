import PIL
def get_pixel_colour(x,y):
    return PIL.ImageGrab.grab().load()[x,y]
