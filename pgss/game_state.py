class GameState:

    #example variable
    __card_count = 0
    
    def __init__(self):
        # setup your variables here
        
        self.cycles_until_win = 
        self.sequence_self = []

        
class Players:
    #position 0 is our position
    num_cards_in_hands = {}
    loop_player = 0
    for x in range(num_players):
        name_player = "num_cards_p" + str(loop_player)
        num_cards_in_hands.update({name_player : 0})
        loop_player += 1

