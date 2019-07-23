class GameState:

    #example variable
    __card_count = 0
    
    def __init__(self):
        # setup your variables here
        
        self.cycles_until_win = []
        self.sequence_self = []
        self.num_cards_in_hands = num_cards_in_hands
        self.cards_of_player = cards_of_player

num_players = 5

num_cards_in_hands = {}
cards_of_player = {}
loop_player = 0
for x in range(num_players):
    name_num_cards = "num_cards_p" + str(loop_player)
    name_player = "player_hands" + str(loop_player)
    cards = []
    num_cards_in_hands.update({name_num_cards : 0})
    cards_of_player.update({name_player : cards_of_player})
    loop_player += 1

            

test = GameState()

print(test.num_cards_in_hands)
print(test.cards_of_player)
