import random
import datastock
import calculsch

class Winset:
    def __init__(self):
        self.winoperator == int(random.choice(rouletteCases))

    def outstats(self):
        self.color = Calculator(self.winoperator).color()
        self.oddeven = Calculator(self.winoperator).is_even()
        self.dozen = Calculator(self.winoperator).dozens()
        self.column = Calculator(self.winoperator).column()
        print("The winning number is : " + str(self.winoperator))
        print("Color: " + str(self.co) + " | " + "Even : " + str(self.ode) + " | " + " Dozen number " + str(
            self.doz) + " | " + " Column number " + str(self.col))
        return self.color, self.oddeven, self.dozen, self.column

