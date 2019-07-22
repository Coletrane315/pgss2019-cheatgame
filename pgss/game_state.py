class GameState:

    #example variable
    __card_count = 0
    
    def __init__(self):
        # setup your variables here
        
        self.cycles_until_win = []
        self.sequence_self = []

num_players = 3

num_cards_in_hands = {}
cards_of_player = {}
loop_player = 0
for x in range(num_players):
    name_player = "num_cards_p" + str(loop_player)
    cards = []
    num_cards_in_hands.update({name_player : 0})
    cards_of_player.update({name_player : cards_of_player})
    loop_player += 1
        
class Players():
    #position 0 is our position
    def __init__(self):
        self.num_cards_in_hands = num_cards_in_hands
        self.cards_of_player = cards_of_player


            

players = Players()

print(players.num_cards_in_hands)
print(players.cards_of_player)
