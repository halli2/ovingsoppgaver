class Sprite:
    neste_ID = 1

    def __init__(self, x_start, y_start, bredde, hoyde):
        self.x_start = x_start
        self.y_start = y_start
        self.bredde = bredde
        self.hoyde = hoyde
        self.__id = Sprite.neste_ID
        Sprite.neste_ID += 1

    @property
    def bredde(self):
        return self.__bredde
        
    @bredde.setter
    def bredde(self, ny_bredde):
        if ny_bredde >= 0:
            self.__bredde = ny_bredde
        else:
            raise ValueError("Bredde kan ikke være negativ!")
        
    @property
    def hoyde(self):
        return self.__hoyde
        
    @hoyde.setter
    def hoyde(self, ny_hoyde):
        if ny_hoyde >= 0:
            self.__hoyde = ny_hoyde
        else:
            raise ValueError("Høyde kan ikke være negativ!")

    @property
    def id(self):
        return self.__id

    def areal(self):
        return self.bredde*self.hoyde

    def er_inni(self, x_koordinat, y_koordinat):
        if x_koordinat < self.x_start:
            return False
        if y_koordinat < self.y_start:
            return False
        if x_koordinat > self.x_start+self.bredde:
            return False
        return True

    def flytt(self, delta_x, delta_y):
        self.x_start += delta_x
        self.y_start += delta_y

    def x_slutt(self):
        return self.x_start + self.bredde

    def y_slutt(self):
        return self.y_start + self.hoyde
