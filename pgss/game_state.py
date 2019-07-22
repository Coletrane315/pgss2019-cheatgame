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

    #this is the number of players!
    number_of_players = 0

    #define hands dictionary as empty for the time being
    hands = {}
    for x in range(number_of_players):
        #where 'n' is the number of cards in the nth player's hand
        n = 0 
        #lst is a dummy variable that will store the cards in the nth player's hand during the loop
        lst = []
        for i in range(n): 
            ele = 0 
            #this loop will append the player's hand with card 'ele' 
            lst.append(ele)
        #Stores lst as the nth player's hand
        hands[x] = lst

    #Now you have a dictionary containing lists of all the player's hands!
