import random;

class Rock:
    def __init__(self):
        self.losesTo = Paper
    
class Paper:
    def __init__(self):
        self.losesTo = Scissors
    
class Scissors:
    def __init__(self):
        self.losesTo = Rock
    

class Game:
    def __init__(self):
        self.generateOpponent()
        
    def generateOpponent(self):
        self.opponent = [Rock(), Paper(), Scissors()][random.randint(0,2)]
        
        self.startGame()
        
    def startGame(self):
        choiceNo = input("Choose Rock(0), Paper(1) or Scissors(2) \n")
        
        choiceIsInvalid = True
        while choiceIsInvalid:
            try:
                choiceObj = [Rock(), Paper(), Scissors()][int(choiceNo)]

                if choiceObj.losesTo == type(self.opponent):
                    print("Ha Loser.")
                elif type(choiceObj) == type(self.opponent):
                    print("draw")
                else:
                    print("Winner winner chicken dinner.")
                    
                choiceIsInvalid = False
            except:
                print("Well that's not really a fucking number though is it?")
            choice = [Rock(), Paper(), Scissors()][int(choiceNo)]
        
Game()
