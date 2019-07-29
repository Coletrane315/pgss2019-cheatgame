

class GameState:
    # the calculated cycles until a win
    __cycles_until_win = 0
    # bot's own sequence
    __bot_sequence = []
    # the number of cards in each hand, dictionary
    __num_cards_hands = {}
    # dict with lists to indicate the known cards of each player
    __cards_of_players = 0
    # the number of cards known in the center
    __num_cards_center = 52 - sum(__num_cards_hands.values())
    # the known cards in the center
    __known_cards_center = []
    # variable of played cards to explain how far the game has progressed
    __num_played_cards = 0
    # variable to loop through the for loop
    __loop_player = 0
    #this loop will create a dictionary of the number of cards in each players hands
    #The bot is player 0 and the dictionary scales with the number of players
    #Expect an error until we can define the number of players from the server
    for x in range(__num_players):
        name_num_cards = "num_cards_p" + str(loop_player)
        name_player = "player_hands" + str(loop_player)
        cards = []
        num_cards_hands.update({name_num_cards : 0})
        cards_of_players.update({name_player : cards_of_players})
        loop_player += 1
            
    def __init__(self):

            self.__cycles_until_win = 0
            self.__bot_sequence = []
            self.__num_cards_hands = __num_cards_hands
            self.__cards_of_players = __cards_of_players
            self.__num_cards_center = 52 - sum(__num_cards_hands.values())
            self.__known_cards_center = []
            self.__num_played_cards = 0


            



