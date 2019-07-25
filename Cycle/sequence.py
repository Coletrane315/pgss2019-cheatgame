class SequenceCalculator:

    @staticmethod
    def calculateSequence(position,num_players):
        start = True
        sequence = [] #The person to the left of the dealer is player 1 and plays an Ace. If one is immidiately to the left of player 1, they are player 2.
        sequence_num = position
        
        while ((position != sequence_num) or (start == True)):
            sequence.append(sequence_num)
            sequence_num = (sequence_num + num_players - 1)%13 + 1
            start = False

        return sequence


    
#change variable names as necessary
