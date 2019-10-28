import random
import re
from calculsch import Calculator
from datastock import Datas


# The Game Class Process


class Game:

    #########################################
    ###Game init and setup/utility functions#
    #########################################

    def __init__(self, player):
        self.round = 0
        self.minbet = 1
        self.tokens = 100
        self.mise = 0
        self.numberlist = [x for x in range(0, 37)]
        self.playername = player

    def getTokens(selfs):
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
        self.startRound()
        self.extendGame()
        self.setvnumber()
        self.roundresult(self.winoperator)
        if self.tokens == 0:
            self.outofstock()
        else:
            pass
        self.round += 1

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
        self.continuer = str(input("Do you want to gamble on anything else ? (y/n) ")).lower()
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
        self.co = Calculator(winop).color()
        self.ode = Calculator(winop).is_even()
        self.doz = Calculator(winop).dozens()
        self.col = Calculator(winop).column()
        # getpairs
        # getsquares
        # getextraifforgot

    def winopinfo(self, winop):
        print("The winning number is : " + str(winop))
        print(
            "Infos - Color: "
            + str(self.co)
            + " | "
            + "Even : "
            + str(self.ode)
            + " | "
            + " Dozen number "
            + str(self.doz)
            + " | "
            + " Column number "
            + str(self.col)        )
        # print double et squares

    ###########################
    ###The Results Functions##
    #########################

    def roundresult(self, vnumber):
        self.resultarray = {}
        self.resultarray['Color'] = self.co
        self.resultarray['Even'] = self.ode
        self.resultarray['Dozen'] = self.doz
        self.resultarray['Column'] = self.col
        print(self.resultarray.items())

    def roundwin(self):
        """Return win"""
        self.endround = 1
        if int(self.multipler) == 2:
            self.gain = float(self.pxmisebet) * int(self.multipler)
            self.bet = float(self.bet) + float(self.gain)
        # Gain for 3x multiplers
        elif int(self.multipler) == 3:
            self.gain = float(self.pxmisebet) * float(self.multipler)
            self.bet = self.bet + self.gain
        # Gain for 6s
        elif int(self.multipler) == 6:
            self.gain = float(self.pxmisebet) * float(self.multipler)
            self.bet = self.bet + self.gain
        # Gain for trios
        elif int(self.multipler) == 12:
            self.gain = float(self.pxmisebet) * float(self.multipler)
            self.bet = self.bet + self.gain
        # Gain for pairs
        elif int(self.multipler) == 18:
            self.gain = float(self.pxmisebet) * float(self.multipler)
            self.bet = self.bet + self.gain
        # Gain for single numbers 0 included
        elif int(self.multipler) == 36:
            self.gain = float(self.pxmisebet) * float(self.multipler)
            self.bet = self.bet + self.gain
        else:
            # Debugg
            print("multipler: " + str(self.multipler))
            print("powerbet: " + str(self.powerbet))
            print("gains: " + str(self.gain))
            print("Error distributing the gains")
            return "error invalid win"
        print("Congrats you won this round !")
        print("Your new amount of credits is : " + str(self.bet))

    def roundloss(self):
        """Return loss"""
        self.endround = 1
        print("Unlucky, you did bet on the wrong number. Better luck next time !")
        print("Your new amount of credits is : " + str(self.bet))

    def roundnul(self):
        self.endround = 1
        print(
            "Unfortunately this round is not a win nor a lose for you, half your bet has been returned to your credits"
        )
        self.gain = float(self.pxmisebet) / 2
        self.bet = self.bet + self.gain

    ######################################
    ###The Results-per-number Functions##
    # bien rajouter le lien pour calcluer un gain total
    ####################################

    def numberissue(self, context):
        if context == "singlenumbers":
            self.singleissue()
        elif context == "doublenumbers":
            self.doubleissue()
        elif context == "trionumbers":
            self.tripleissue()
        elif context == "sixnumbers":
            self.sixissue()
        elif context == "dozens":
            self.dozensissue()
        elif context == "columns":
            self.columnissue()
        elif context == "half":
            self.halfissue()
        elif context == "color":
            self.colorissue()
        elif context == "oddeven":
            self.odevissue()

    #############################
    ###The BetManage Functions##
    ###########################

    # Confirmise - Checks if player respects betting rules
    def confirmise(self):
        isable = self.misetyper()
        if isable is True:
            isvalid = self.misevalider(self.pxmisebet)
            if isvalid is True:
                print("You Gambled " + str(self.pxmisebet) + " token(s)") # Django : {[self.pxnumber]}
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
            self.doublenumpicker()
        elif choice in ("triple, 3"):
            self.trionumpicker()
        elif choice in ("square, 4"):
            print("Sorry squares are unavailable rn")
        elif choice in ("six, 5"):
            self.sixnumpicker()
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

    # 1 Number Picker
    def singlenumpicker(self):
        self.context = 36
        enterpxnumber = self.pxnumbertyper()
        if enterpxnumber is True:
            print("You are gambling on number " + str(self.pxnumber))
            validarray = self.confirmise()
            if validarray is True:
                self.addgamble(self.pxnumber, self.tokenmise)
            else:
                pass
        else:
            self.singlenumpicker()

    # 2 Number Picker

    # 3 Number Picker

    # 4 Number Picker

    # 6 Number Picker

    # Color Number Picker

    # Half Number Picker

    # Dozens Number Picker

    # Columns Number Picker

    # Odd-Even Number Picker

    # Bet Multiplicator Function
    """def multatr(self, context):
        if context == "singlenumber":
            self.multipler = 36.0
        elif context == "doublenumers":
            self.multipler = 18.0
        elif context == "trionumbers":
            self.multipler = 12.0
        elif context == "square":
            self.multipler = 9.0
        elif context == "sixnumbers":
            self.multipler = 6.0
        elif context in ("dozens, columns"):
            self.multipler = 3.0
        elif context in ("half, color, oddeven"):
            self.multipler = 2.0
        else:
            return KeyError
        return self.multipler"""

    # Add a gamble dict key
    def addgamble(self, number, bet):
        self.gamblify[number] = bet

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

    # Game infos & MenuLater
    def gameinfo(self):
        print(
            "The playable formats are listed bellow [Type x number to gamble on x format]: ")
        print(" ")
        print(
            "[1] Single (1:36) | [2] Double (1:18) | [3] Triple (1:12) | [4] Square (1:9) | [5] Six (1:6) "
        )
        print(
            "[6] Dozen (1:3) | [7] Column (1:3) | [8] Half (1:2) | [9] Even/Odd (1:2) | [0] Color (1:2) ")
        print(" ")
        print(str(self.playername) + "'s game infos - Round : " + str(self.round) + " - Current Tokens : " + str(self.tokens) + " - Minimum Bet : " + str(self.minbet))
        print(
            "--------------------------------------------------------------------------------------------------")

    # Ingame infos about current gambles
    def gamblesinfo(self):
        print(
            "--------------------------------------------------------------------------------------------------")
        print("Current token stock : " + str(self.tokens))
        print("Current gambled values : ")
        for i in self.gamblify.items():
            print("Val: "+ str(i[0]) + " - Bet: " + str(i[1]))
        print(
            "--------------------------------------------------------------------------------------------------")

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
