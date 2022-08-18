class BTEB:
    def __init__(self,Technology, Seat, Shift,s):
        self.technology = Technology
        self.seat = Seat
        self.shift = Shift
        self.S = s

    def BBPI(self):
        print("%s ----- %d ------ %d"%(self.technology, self.seat,self.shift))



if __name__ == "__main__":
    s = str(input()).lower()
    infor =
    if self.S == "bbpi"
        info = BTEB("Computer Technology",200, 2)
        info2 = BTEB("Electromedical Technology",100, 2)
        info3 = BTEB("Refrigeration & Air Condition Technology",100, 2)
        info4 = BTEB("Architecture and Interior Design Technology", 100, 2)

        print("Technology ----- Seat ------ Shift :")
        info.BBPI()
        info2.BBPI()
        info3.BBPI()
        info4.BBPI()