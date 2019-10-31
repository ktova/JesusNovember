class Calculator:

    def __init__(self, number):
        self.number = number
        self.rm1 = number - 1
        self.rm2 = number - 2
        self.rm3 = number - 3
        self.rm4 = number - 4
        self.rm5 = number - 5
        self.ra1 = number + 1
        self.ra2 = number + 2
        self.ra3 = number + 3
        self.ra4 = number + 4
        self.ra5 = number + 5

    def color(self):
        if self.number == 0:
            return 0
        elif (self.number >= 1 and self.number <= 10) or (
            self.number >= 19 and self.number <= 28
        ):
            if self.number % 2 == 0:
                return "black"
            else:
                return "red"
        elif (
            self.number >= 11
            and self.number <= 18
            or (self.number >= 29 and self.number <= 36)
        ):
            if self.number % 2 == 0:
                return "red"
            else:
                return "black"

    def is_even(self):
        if self.number == 0:
            return 0
        else:
            if self.number % 2 == 0:
                return "even"
            if self.number % 2 == 1:
                return "odd"
            #return self.number % 2 == 0 - production record

    def half(self):
        if self.number == 0:
            return 0
        else:
            if self.number < 19:
                return "first"
            if self.number > 18:
                return "last"

    def column(self):
        if self.number == 0:
            return 0
        else:
            result_of_division = self.number % 3
            if result_of_division == 0:
                return 3
            else:
                return result_of_division

    def dozens(self):
        if self.number == 0:
            return 0
        elif self.number >= 1 and self.number <= 12:
            return 1
        elif self.number >= 13 and self.number <= 24:
            return 2
        elif self.number >= 25 and self.number <= 36:
            return 3

    def pair(self):
        spr1 = []
        spr2 = []
        spr3 = []
        spr4 = []
        if self.number == 0:
            return 0
        else:
            if self.number == 1:
                spr1 = [1, 2]
                spr2 = [1, 4]
            elif self.number == 2:
                spr1 = [1, 2]
                spr2 = [2, 3]
                spr3 = [2, 5]
            elif self.number == 3:
                spr1 = [2, 3]
                spr2 = [3, 6]
            elif self.number == 34:
                spr1 = [31, 34]
                spr2 = [34, 35]
            elif self.number == 35:
                spr1 = [32, 35]
                spr2 = [34, 35]
                spr3 = [35, 36]
            elif self.number == 36:
                spr1 = [33, 36]
                spr2 = [35, 36]
            elif self.number % 3 == 0:
                spr1 = [self.rm3, self.number]
                spr2 = [self.rm1, self.number]
                spr3 = [self.number, self.ra3]
            elif self.number % 3 == 1:
                spr1 = [self.rm3, self.number]
                spr2 = [self.number, self.ra1]
                spr3 = [self.number, self.ra3]
            elif self.number % 3 == 2:
                spr1 = [self.rm3, self.number]
                spr2 = [self.rm1, self.number]
                spr3 = [self.number, self.ra1]
                spr4 = [self.number, self.ra3]
            return spr1, spr2, spr3, spr4

    def square(self):
        sqr1 = []
        sqr2 = []
        if self.number == 0:
            return 0
        else:
            if self.number == 1:
                self.sqr1 = [1, 2, 4, 5]
            elif self.number == 3:
                self.sqr1 = [2, 3, 5, 6]
            elif self.number == 34:
                self.sqr1 = [31, 32, 34, 35]
            elif self.number == 36:
                self.sqr1 = [32, 33, 35, 36]
            else:
                if self.number % 3 == 1:
                    sqr1 = [self.rm3,self.rm2,self.number,self.ra1]
                    sqr2 = [self.number,self.ra1,self.ra2,self.ra3]
                elif self.number % 3 == 2:
                    sqr1 = [self.rm1,self.number,self.ra2,self.ra3]
                    sqr2 = [self.number,self.ra1,self.ra3,self.ra4]
                elif self.number % 3 == 0:
                    sqr1 = [self.rm3,self.rm1,self.number,self.ra4]
                    sqr2 = [self.rm1,self.number,self.ra2,self.ra3]
            return sqr1, sqr2

    def six(self):
        sxt1 = []
        sxt2 = []
        if self.number == 0:
            return 0
        else:
            if self.number <= 3:
                sxt1 = {1, 2, 3, 4, 5, 6}
            elif self.number >= 34:
                sxt1 = {31, 32, 33, 34, 35, 36}
            else:
                if self.number % 3 == 1:
                    sxt1 = [self.rm3,self.rm2,self.rm1,self.number,self.ra1,self.ra2]
                    sxt2 = [self.number,self.ra1,self.ra2,self.ra3,self.ra4,self.ra5]
                elif self.number % 3 == 2:
                    sxt1 = [self.rm4,self.rm3,self.rm2,self.rm1,self.number,self.ra1]
                    sxt2 = [self.rm1,self.number,self.ra1,self.ra2,self.ra3,self.ra4]
                elif self.number % 3 == 0:
                    sxt1 = [self.rm5,self.rm4,self.rm3,self.rm2,self.rm1,self.number]
                    sxt2 = [self.rm2,self.rm1,self.number,self.ra1,self.ra2,self.ra3]
            return sxt1, sxt2