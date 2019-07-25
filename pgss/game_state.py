class GameState:

    #example variable
    __card_count = 0
    
    def __init__(self):

        #I have no idea what this first variable does but I was told to put it in.
        #If it's supposed to be a number instead of a list go ahead and change it.
        self.cycles_until_win = []
        self.sequence_self = []
        self.num_cards_hands = num_cards_in_hands
        self.cards_of_player = cards_of_player
        self.num_cards_center = 52 - sum(num_cards_hands.values())
        self.known_cards_center = []
        self.num_played_cards = 0

num_players = 4

num_cards_hands = {}
cards_of_player = {}
loop_player = 0
#this loop will create a dictionary of the number of cards in each players hands
#The bot is player 0 and the dictionary scales with the number of players
for x in range(num_players):
    name_num_cards = "num_cards_p" + str(loop_player)
    name_player = "player_hands" + str(loop_player)
    cards = []
    num_cards_hands.update({name_num_cards : 0})
    cards_of_player.update({name_player : cards_of_player})
    loop_player += 1

            



