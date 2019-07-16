#!/bin/bash
# Ace = 1
# 2 = 2
# ...
# 10 = 10
# Jack = 11
# Queen = 12
# King = 13
class cheatingTheCheat:
    def __init__(self, players, position):
        self.reset()
        self.players = players
        self.position = position
    
    def reset(self):
        self.players = 0
        self.position = 0
        self.sequence = []
  
    def main(self):
        self.findSequence()
        print (self.sequence)
        
    def findSequence(self):
        start = True
        sequenceTemp = self.position #The person to the left of the dealer is player 1 and plays an Ace. If one is immidiately to the left of player 1, they are player 2. 
        while ((self.position != sequenceTemp) or (start == True)):
            self.sequence.append(sequenceTemp)
            sequenceTemp = (sequenceTemp + self.players -1)%13 + 1
            start = False

nP = input('How many people are playing? ')
try:
    nP = int(nP) 
except ValueError:
    print("Invalid number")
pV = input('If the player to the left of the dealer is position 1 and the player to the left of them is position 2, what is your position? ')
try:
    pV = int(pV)
except ValueError:
    print("Invalid number")
run = cheatingTheCheat(nP, pV)
run.main()
