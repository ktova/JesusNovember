import random
import re
from calculsch import Calculator
from radnum import Keynum
from datastock import Datas

#The Game Class Process

class Game():

    #########################################
   ###Game init and setup/utility functions#
  #########################################


    def __init__(self):
        self.round = 0
        self.minbet = 1
        self.tokens = 100
        self.playername = "Player1"

    def getTokens(selfs):
        print("Votre nombre de jetons est de : ")
        return self.tokens

    def setTokens(self, ntok):
        self.tokens = ntok
        print("Votre nombre de jetons est de : " + self.token)

    def getroundbet(self):
        return self.round, self.minbet

    def allowtoplay(self):
        if (self.tokens > 0):
            return True
        else:
            return False

    #Starts the game
    def startRound(self):
        self.allow = self.allowtoplay()
        if self.allow is True:
            self.gameinfo()
            self.gamepicker()
        else:
            self.outofstock()

    #Ends the game
    def outofstock(self):
        print("You are running out of tokens, the game is over until you inject more pa$$i0n")
        return False

    ##################
   ##Game core funcs#
  #################

    #Pick a format
    def gamepicker(self):
        self.gambled = {}
        x = 1
        self.securepick = self.gametyper()
        if self.securepick is True:
            self.gameselector(self.gamepicked)
        else:
            return ChildProcessError

    #Chose another format // Not released yet
    def continueur(self):
        print("Do you want to gamble on anything else ? (y/n)")
        self.continuer = str(input()).lower()
        if self.continuer == "y":
            self.multigamepicker(self.multigambleask)
            return True
        elif self.continuer == "n":
            return False
        else:
            print("invalid response, we're processing to the end of the current round")

    #Adds new queries if player picks multiple-gambling
    def multigamepicker(self, mga):
        if mga is True:
            x+=1
            self.extragame = str(input()).lower()
            self.gambled['x'] = self.extragame
        else:
            pass

    #############################
    ###The BetManage Functions##
    ###########################

    #Confirmise - Checks if player respects betting rules
    def confirmise(self):
        self.pxmisebet = float(input())
        while self.pxmisebet > 0.5:
            if self.pxmisebet > self.tokens:
                print(" Thats way too much for your wallet sir ")
                self.pxmisebet = float(input())
            else:
                print("You gambled " + str(self.pxmisebet) + " tokens this round")
                return self.pxmisebet
        self.mise(self.pxmisebet)

    # Retrieve gambled tokens during the round - has to be optimized for multitype gambling
    def mise(self, pxmise):
        if pxmise >= 0.5:
            self.bet = float(self.bet) - float(self.pxmisebet)
        else:


    ###############################
    ###The Selectnumbr Functions##
    #############################

    #Select the player's desired format - could be optimized throwing only context followed by
    #A type picker function but not able to make a proper script for the moment
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

    # Selects the player's number out of the selected format
    # Could be optimized later

    # 1 Number Picker
    def singlenumpicker(self):
        self.context = "singlenumber"
        self.multatr(self.context)
        print("Which number do you want to gamble on ?")
        self.pxnumber = input()
        while int(self.pxnumber) >= 0:
            if 0 <= int(self.pxnumber) < 37:
                print("You gambled on number " + str(self.pxnumber))
            else:
                print(" You must chose a number between 0 and 36 ")
                self.pxnumber = input()
            break
        print(f"How many tokens are you gonna bet on {[self.pxnumber]}")
        self.confirmise()

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
    def multatr(self, context):
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
        return self.multipler

    ###############################
    ###The Securecheck Functions##
    #############################

    #Select a game format from gamepicker selection
    def gamesecurecheck(self, arg):
        if arg in Datas.games:
            return True
        else:
            print("You submitted an invalid gamemode, you may try again")
            self.gametyper()

    ##############################
    ###The Securetype Functions##
    ############################

    def gametyper(self):
        self.gamepicked = str(input()).lower()
        self.gamesecurecheck(self.gamepicked)

    #############################
    ###The Game Menu Functions##
    ###########################

    #mdr
    def welcome(self):
        print("")
        print(
            "                                       –––––––––––––––––––––––––––––––––––––––––––––––––--                  ")
        print(
            "                                      |                                                   |                   ")
        print(
            "                                      |                  Yeezus Loulette                  |                   ")
        print(
            "                                      |                                                   |                   ")
        print(
            "                                       –––––––––––––––––––––––––––––––––––––––––––––––––--                   ")
        print("")

    #Game infos & MenuLater
    def gameinfo(self):
        print("The playable formats are listed bellow [Type x number to play x format]: ")
        print(" ")
        print("[1] Single (1:36) | [2] Double (1:18) | [3] Triple (1:12) | [4] Square (1:9) | [5] Six (1:6) ")
        print(" ")
        print("[6] Dozen (1:3) | [7] Column (1:3) | [8] Half (1:2) | [9] Even/Odd (1:2) | [0] Color (1:2) ")
        print('--------------------------------------------------------------------------------------------------')

    ################################
   ###The Game Instance Functions##
  ################################

def startGame():
    new_game = Game()
    new_game.welcome()
    new_game.startRound()

    #####################
   ###The Game Starter##
  #####################

startGame()