class GameState:

    __cycles_until_win = []
    __sequence_self = []
    __num_cards_hands = {}
    __cards__player = 0
    __num_cards_center = 52 - sum(__num_cards_hands.values())
    __known_cards_center = []
    __num_played_cards = 0
    __num_cards_hands = {}
    __cards_of_player = {}
    __loop_player = 0
    #this loop will create a dictionary of the number of cards in each players hands
    #The bot is player 0 and the dictionary scales with the number of players
    #Expect an error until we can define the number of players from the server
    for x in range(__num_players):
        name_num_cards = "num_cards_p" + str(loop_player)
        name_player = "player_hands" + str(loop_player)
        cards = []
        num_cards_hands.update({name_num_cards : 0})
        cards_of_player.update({name_player : cards_of_player})
        loop_player += 1
            
    def __init__(self):

            self.cycles_until_win = 0
            self.sequence_self = []
            self.num_cards_hands = __num_cards_in_hands
            self.cards_of_player = __cards_of_player
            self.num_cards_center = 52 - sum(__num_cards_hands.values())
            self.known_cards_center = []
            self.num_played_cards = 0

num_players = 4



            



