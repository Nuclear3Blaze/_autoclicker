import time as t,pygame as p
class Clicker:
    def __init__(self):
        p.init()
        self.Starter()
    def Starter(self):
        while True:
            print("1. Hoard\n2. Other User\n3. Personal\n4. Pokerus\n5. Random User\n6. Help")
            typ = input("Enter the number you want to do: ")
            if typ == "1":
                import Hoard
            elif typ == "2":
                import Other
            elif typ == "3":
                import Personal
            elif typ == "4":
                import Pokerus
            elif typ == "5":
                import Pokerus
            elif typ == "6":
                import Help
clicker = Clicker()
