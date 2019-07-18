class SequenceCalculator:

    def calculateSequence(self,game_state):
        start = True
        sequenceTemp = self.position #The person to the left of the dealer is player 1 and plays an Ace. If one is immidiately to the left of player 1, they are player 2.
        while ((self.position != sequenceTemp) or (start == True)):
            self.sequence.append(sequenceTemp)
            sequenceTemp = (sequenceTemp + self.players -1)%13 + 1
            start = False
#change variable names as necessary
