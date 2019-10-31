import random
from calculsch import Calculator
from datastock import Datas

# The Game Class Process


class Game:

    #########################################
    ###Game init and setup/utility functions#
    #########################################

    def __init__(self, player):
        self.state = 1
        self.round = 0
        self.minbet = 1
        self.tokens = 100
        self.mise = 0
        self.numberlist = [x for x in range(0, 37)]
        self.playername = player

    def getTokens(self):
        print("Votre nombre de jetons est de : ")
        return self.tokens

    def setTokens(self, ntok):
        self.tokens = ntok
        print("Votre nombre de jetons est de : " + self.token)

    def getroundbet(self):
        return self.round, self.minbet

    def allowtoplay(self):
        if self.tokens > 0:
            return True
        else:
            return False

    ###################
    ##Game core funcs#
    #################

    # Starts the game
    def roundSet(self):
        while self.state == 1:
            self.round += 1
            self.startRound()
            self.extendGame()
            self.setvnumber()
            self.roundresult(self.winoperator)
            if self.tokens == 0:
                self.outofstock()
            else:
                pass

    # Starting round
    def startRound(self):
        allow = self.allowtoplay()
        if allow is True:
            self.gameinfo()
            self.gamepicker()
        else:
            self.outofstock()

    # Ends the game
    def outofstock(self):
        print(
            "You are running out of tokens, the game is over until you inject more pa$$i0n"
        )
        self.state = 0
        return exit()

    # Pick a format
    def gamepicker(self):
        self.gamblify = {}
        canstartplay = self.gametyper()
        if canstartplay is True:
            self.gameselector(self.gamepicked)
        else:
            self.gamepicker()

    # Extend game function if player wants to gamble more
    def extendGame(self):
        extender = True
        while extender is True:
            if self.tokens > 0:
                extender = self.extragamepicker()
            else:
                extender = False

    # Chose another format // Not released yet
    def continueur(self):
        self.continuer = str(
            input("Do you want to gamble on anything else ? (y/n) ")
        ).lower()
        if self.continuer == "y":
            return True
        else:
            return False

    # Adds new queries if player picks multiple-gambling
    def extragamepicker(self):
        continuer = self.continueur()
        if continuer is True:
            canstartplay = self.gametyper()
            if canstartplay is True:
                self.gameselector(self.gamepicked)
                return True
            else:
                return True
        else:
            return False

    ###########################
    ###The WinNumb Functions##
    #########################

    def setvnumber(self):
        self.winoperator = int(random.choice(self.numberlist))
        self.numberproperties(self.winoperator)
        self.winopinfo(self.winoperator)

    def numberproperties(self, winop):
        self.winop = winop
        self.co = Calculator(winop).color()
        self.ode = Calculator(winop).is_even()
        self.alf = Calculator(winop).half()
        self.doz = Calculator(winop).dozens()
        self.col = Calculator(winop).column()
        self.spr = Calculator(winop).pair()
        self.sqr = Calculator(winop).square()
        self.sxt = Calculator(winop).six()

    def winopinfo(self, winop):
        print("The winning number is : " + str(winop))
        print(
            "Infos - Color: "
            + str(self.co)
            + " | "
            + "Even : "
            + str(self.ode)
            + " | "
            + "Half : "
            + str(self.alf)
            + " | "
            + " Dozen number "
            + str(self.doz)
            + " | "
            + " Column number "
            + str(self.col)
            + "| Pairs : "
            + str(self.spr)
            + "| Square(s) : "
            + str(self.sqr)
            + "| Six(s) : "
            + str(self.sxt)
        )
        # print double et squares

    ###########################
    ###The Results Functions##
    #########################

    def roundresult(self, vnumber):
        self.resultarray = {}
        self.resultarray["Number"] = self.winop
        self.resultarray["Color"] = self.co
        self.resultarray["Even"] = self.ode
        self.resultarray["Half"] = self.alf
        self.resultarray["Dozen"] = self.doz
        self.resultarray["Column"] = self.col
        self.resultarray["Pairs"] = self.spr
        self.resultarray["Square"] = self.sqr
        self.resultarray["Six"] = self.sxt
        self.comparearr()

    def comparearr(self):
        print(self.resultarray.items())
        print(self.gamblify.items())
        for i in self.resultarray.items():
            for l in self.gamblify.items():
                if l[0] in i:
                    gains = l[1][0]*l[1][1]
                    self.tokens += gains
                    print(str(i[0]) + " - " + str(l[0]) + " - " + str(l[1][0]) + "-" + str(l[1][1]) )
                else:
                    pass

    #############################
    ###The BetManage Functions##
    ###########################

    # Confirmise - Checks if player respects betting rules
    def confirmise(self):
        isable = self.misetyper()
        if isable is True:
            isvalid = self.misevalider(self.pxmisebet)
            if isvalid is True:
                print(
                    "You Gambled " + str(self.pxmisebet) + " token(s)"
                )  # Django : {[self.pxnumber]}
                self.tokenmise = self.pxmisebet
                return True
            else:
                print("You don't have enough tokens")
                return False
        else:
            return False

    # Retrieve gambled tokens during the round - has to be optimized for multitype gambling
    def misevalider(self, pmise):
        if self.tokens - pmise >= 0:
            self.tokens -= pmise
            return True
        else:
            return False

    ###############################
    ###The Selectnumbr Functions##
    #############################

    # Select the player's desired format - could be optimized throwing only context followed by
    # A type picker function but not able to make a proper script for the moment
    def gameselector(self, choice):
        if choice in ("color, 0"):
            self.colorpicker()
        elif choice in ("single, 1"):
            self.singlenumpicker()
        elif choice in ("double, 2"):
            self.pairpicker()
        elif choice in ("square, 4"):
            self.squarepicker()
        elif choice in ("six, 5"):
            self.sixtpicker()
        elif choice in ("dozen, 6"):
            self.dozenpicker()
        elif choice in ("column, 7"):
            self.columnpicker()
        elif choice in ("half, 8"):
            self.halfpicker()
        elif choice in ("even, odd, 9"):
            self.oddevenpicker()
        self.gamblesinfo()

    # Selects the player's number out of the selected format

    # Color Number Picker
    def colorpicker(self):
        self.context = 2
        entercolor = self.colortyper()
        if entercolor is True:
            print("You are gambling on color " + str(self.pxcolor))
            validarray = self.confirmise()
            if validarray is True:
                self.addgamble(self.pxcolor, self.tokenmise, self.context)
            else:
                pass
        else:
            self.colorpicker()

    # Half Number Picker
    def halfpicker(self):
        self.context = 2
        enterhalf = self.halftyper()
        if enterhalf is True:
            print("You are gambling on half " + str(self.pxhalf))
            validarray = self.confirmise()
            if validarray is True:
                self.addgamble(self.pxhalf, self.tokenmise, self.context)
            else:
                pass
        else:
            self.halfpicker()

    # Odd-Even Number Picker
    def oddevenpicker(self):
        self.context = 2
        enterodev = self.odevtyper()
        if enterodev is True:
            print("You are gambling on " + str(self.pxodev) + " numbers")
            validarray = self.confirmise()
            if validarray is True:
                self.addgamble(self.pxodev, self.tokenmise, self.context)
            else:
                pass
        else:
            self.oddevenpicker()

    # Dozens Number Picker
    def dozenpicker(self):
        self.context = 3
        enterdozen = self.dozentyper()
        if enterdozen is True:
            print("You are gambling on dozen n°" + str(self.pxdoz))
            validarray = self.confirmise()
            if validarray is True:
                self.pxdoz = "d" + str(self.pxdoz)
                self.addgamble(self.pxdoz, self.tokenmise, self.context)
            else:
                pass
        else:
            self.dozenpicker()

    # Columns Number Picker
    def columnpicker(self):
        self.context = 3
        entercolumn = self.columntyper()
        if entercolumn is True:
            print("You are gambling on column n°" + str(self.pxcol))
            validarray = self.confirmise()
            if validarray is True:
                self.pxcol = "c" + str(self.pxcol)
                self.addgamble(self.pxcol, self.tokenmise, self.context)
            else:
                pass
        else:
            self.columnpicker()

    # 1 Number Picker
    def singlenumpicker(self):
        self.context = 36
        enterpxnumber = self.pxnumbertyper()
        if enterpxnumber is True:
            print("You are gambling on number " + str(self.pxnumber))
            validarray = self.confirmise()
            if validarray is True:
                self.addgamble(self.pxnumber, self.tokenmise, self.context)
            else:
                pass
        else:
            self.singlenumpicker()

    # 2 Number Picker
    def pairpicker(self):
        self.context = 18
        enterpxnumber = self.pairtyper()
        if enterpxnumber is True:
            print("You are gambling on pair " + str(self.pxpair))
            validarray = self.confirmise()
            if validarray is True:
                self.addgamble(self.pxpair, self.tokenmise, self.context)
            else:
                pass
        else:
            self.pairpicker()

    # 4 Number Picker
    def squarepicker(self):
        self.context = 9
        enterpxnumber = self.squaretyper()
        if enterpxnumber is True:
            print("You are gambling on square " + str(self.square))
            validarray = self.confirmise()
            if validarray is True:
                self.addgamble(self.square, self.tokenmise, self.context)
            else:
                pass
        else:
            self.squarepicker()

    # 6 Number Picker
    def sixtpicker(self):
        self.context = 6
        enterpxnumber = self.sixtyper()
        if enterpxnumber is True:
            print("You are gambling on sixs " + str(self.six))
            validarray = self.confirmise()
            if validarray is True:
                self.addgamble(self.six, self.tokenmise, self.context)
            else:
                pass
        else:
            self.sixtpicker()

    # Add a gamble dict key
    def addgamble(self, number, bet, multipler):
        self.gamblify[number] = bet, multipler

    ###############################
    ###The Securecheck Functions##
    #############################

    # Select a game format from gamepicker selection
    def gamesecurecheck(self, arg):
        if arg in Datas.games:
            return True
        else:
            print("Please select a valid gamemode")
            return False

    # Confirms that the bet is valid
    def pxmisesecurecheck(self, pxmise):
        float(self.pxmisebet)
        if pxmise >= 0.5:
            if pxmise > self.tokens:
                print(" Thats way too much for your wallet sir ")
                return False
            else:
                return True
        else:
            print("Please respect the minimum betting rule")
            return False

    # Confirm valid number
    def pxnumsecurechecker(self, pxnumber):
        if 0 <= pxnumber < 37:
            return True
        else:
            print("Please enter a number between 0 and 36")
            return False

    def colorsecurecheck(self, pxcolor):
        if pxcolor in {"red", "black"}:
            return True
        else:
            print("Please enter a valid color")
            return False

    def halfsecurecheck(self, pxhalf):
        if pxhalf in {"first","last"}:
            return True
        else:
            print("Please enter a valid half")
            return False

    def odevsecurechecker(self, pxodev):
        if pxodev in {"odd", "even"}:
            return True
        else:
            print("Please enter a valid value")
            return False

    def dozensecurechecker(self, pxnumber):
        if 0 < pxnumber < 4:
            return True
        else:
            print("Please enter a valid dozen")
            return False

    def columnsecurechecker(self, pxnumber):
        if 0 < pxnumber < 4:
            return True
        else:
            print("Please enter a valid column")
            return False

    def pairsecurechecker(self, pxstring):
        arg = pxstring[0]
        validpair = Calculator(arg).pair()
        if pxstring in validpair:
            return True
        else:
            print("Please enter a valid pair")
            return False

    def squaresecurechecker(self, pxstring):
        arg = pxstring[0]
        validpair = Calculator(arg).square()
        if pxstring in validpair:
            return True
        else:
            print("Please enter a valid square")
            return False

    def sixsecurechecker(self, pxstring):
        arg = pxstring[0]
        validpair = Calculator(arg).six()
        if pxstring in validpair:
            return True
        else:
            print("Please enter a valid six")
            return False

    ##############################
    ###The Securetype Functions##
    ############################

    def gametyper(self):
        self.gamepicked = str(input("Which format do you want to gamble on ? ")).lower()
        issecure = self.gamesecurecheck(self.gamepicked)
        if issecure is True:
            return True
        else:
            return False

    def misetyper(self):
        try:
            self.pxmisebet = float(input("How many tokens are you gonna bet ? "))
            issecure = self.pxmisesecurecheck(self.pxmisebet)
            if issecure is True:
                return True
            else:
                return False
        except ValueError:
            print("Please enter a number as a value")

    def pxnumbertyper(self):
        try:
            self.pxnumber = int(input("Which number do you want to gamble on ? "))
            issecure = self.pxnumsecurechecker(self.pxnumber)
            if issecure is True:
                return True
            else:
                return False
        except ValueError:
            print("Please enter a number as value")

    def colortyper(self):
        self.pxcolor = str(
            input("Which color do you want to gamble on [red|black]?")
        ).lower()
        issecure = self.colorsecurecheck(self.pxcolor)
        if issecure is True:
            return True
        else:
            return False

    def halftyper(self):
        self.pxhalf = str(
            input(
                "Do you want to gamble on the first (1-18) half or the last half (19-36) ?"
            )
        ).lower()
        issecure = self.halfsecurecheck(self.pxhalf)
        if issecure is True:
            return True
        else:
            print("Please enter a valid half [first - last]")
            return False

    def odevtyper(self):
        self.pxodev = str(
            input("Do you want to bet on an odd number or an even one ?")
        ).lower()
        issecure = self.odevsecurechecker(self.pxodev)
        if issecure is True:
            return True
        else:
            return False

    def dozentyper(self):
        try:
            self.pxdoz = int(input("Which dozen do you want to gamble on ?"))
            issecure = self.dozensecurechecker(self.pxdoz)
            if issecure is True:
                return True
            else:
                return False
        except ValueError:
            print("Please enter a valid dozen [1 - 2 - 3]")

    def columntyper(self):
        try:
            self.pxcol = int(input("Which column do you want to gamble on ?"))
            issecure = self.columnsecurechecker(self.pxcol)
            if issecure is True:
                return True
            else:
                return False
        except ValueError:
            print("Please enter a valid column [1 - 2 - 3]")

    def pairtyper(self):
        self.pxpair = []
        self.gamehelper()
        try:
            pairnum1 = int(input("Which pair do you want to gamble on e.g[1,2]? Type the lowest number : "))
            pairnum2 = int(input("Now Type the highest number : "))
            self.pxpair.append(pairnum1)
            self.pxpair.append(pairnum2)
            issecure = self.pairsecurechecker(self.pxpair)
            if issecure is True:
                return True
            else:
                return False
        except ValueError:
            print("Please enter a valid pair or number")

    def squaretyper(self):
        self.square = []
        self.gamehelper()
        try:
            sqnum1 = int(input("Which square do you want to gamble on e.g[4,5,7,8]? Type the lowest number : "))
            sqnum2 = int(input("Type the second lowest number : "))
            sqnum3 = int(input("Type the second highest number : "))
            sqnum4 = int(input("Type the highest number : "))
            self.square.append(sqnum1)
            self.square.append(sqnum2)
            self.square.append(sqnum3)
            self.square.append(sqnum4)
            issecure = self.squaresecurechecker(self.square)
            if issecure is True:
                return True
            else:
                return False
        except ValueError:
            print("Please enter a valid square or number")

    def sixtyper(self):
        self.six = []
        self.gamehelper()
        try:
            sixt1 = int(input("Which pair do you want to gamble on e.g[1,2,3,4,5,6]? Type the lowest number : "))
            sixt2 = int(input("Type the 2nd number of the string : "))
            sixt3 = int(input("Type the 3rd number of the string : "))
            sixt4 = int(input("Type the 4th number of the string : "))
            sixt5 = int(input("Type the 5th number of the string : "))
            sixt6 = int(input("Type the 6th number of the string : "))
            self.six.append(sixt1)
            self.six.append(sixt2)
            self.six.append(sixt3)
            self.six.append(sixt4)
            self.six.append(sixt5)
            self.six.append(sixt6)
            issecure = self.sixsecurechecker(self.six)
            if issecure is True:
                return True
            else:
                return False
        except ValueError:
            print("Please enter a valid six or number")

    #############################
    ###The Game Menu Functions##
    ###########################

    # mdr
    def welcome(self):
        print("")
        print(
            " –––––––––––––––––––––––––––––––––––––––––––––––––--––––––––––––––––––––––––                  "
        )
        print(
            "|                                                                          |                   "
        )
        print(
            "|                             Yeezus Roulette                              |                   "
        )
        print(
            "|                                                                          |                   "
        )
        print(
            " –––––––––––––––––––––––––––––––––––––––––––––––––--––––––––––––––––––––––––                   "
        )
        print("")
        print(
            "The playable formats are listed bellow [Type format's number or name]: "
        )
        print(
            "Warning : double / six numbers gambles are not working"
        )

    def gamehelper(self):
        print("–––––––––––––––––––––––––––––––––––––––––––––––––--––––––––––––––––––––––––")
        print("Game Table :")
        print("––––––––––––––––––––––––––––––––––––––––--------––––––––")
        print(
            "3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 |"
        )
        print("––––––––––––––––––––––––––––––––––––––––--------––––––––")
        print(
            "2 | 5 | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 |"
        )
        print("––––––––––––––––––––––––––––––––––––––––--------––––––––")
        print(
            "1 | 4 | 7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 |"
        )
        print("–––––––––––––––––––––––––––––––––––––––––––––––––--––––––––––––––––––––––––")

    # Game infos & MenuLater
    def gameinfo(self):
        print(
            "--------------------------------------------------------------------------------------------------"
        )
        print(
            "[1] Single (1:36) | [2] Double (1:18) | [4] Square (1:9) | [6] Six (1:6) "
        )
        print(
            "[0] Color (1:2) | [6] Dozen (1:3) | [7] Column (1:3) | [8] Half (1:2) | [9] Even/Odd (1:2) "
        )
        print(" ")
        print(
            str(self.playername)
            + "'s game infos - Round : "
            + str(self.round)
            + " - Current Tokens : "
            + str(self.tokens)
            + " - Minimum Bet : "
            + str(self.minbet)
        )
        print(
            "--------------------------------------------------------------------------------------------------"
        )

    # Ingame infos about current gambles
    def gamblesinfo(self):
        print(
            "--------------------------------------------------------------------------------------------------"
        )
        print("Current token stock : " + str(self.tokens))
        print("Current gambled values : ")
        for i in self.gamblify.items():
            print("Val: " + str(i[0]) + " - Bet: " + str(i[1]))
        print(
            "--------------------------------------------------------------------------------------------------"
        )

    ################################ End of Game class


###The Game Instance Functions##
################################


def startGame():
    new_game = Game(input("Hello player what is your name ? "))
    new_game.welcome()
    new_game.roundSet()

    #####################


###The Game Starter##
#####################

startGame()
