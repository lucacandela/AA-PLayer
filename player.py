from unit import Unit


class AAPlayer:
    def __init__(self, units: list, yen: int, keybrd):
        self.units = Unit[units]
        self.yen = yen
        self.keybrd = keybrd

    def changeYen(self,yen):
        self.yen = yen
    
    def changeUnits(self, units):
        self.units = units

    def checkYen(self):
        yen = "computer vision pointed at yen field"
        return 