class GameState:

    #list of player objects representing players in the game
    __players = []

    #player object which is the bot, also represented in __players
    __bot = Player()

    #the number of cards in the center pile
    __num_cards_center=0

    #the known cards in the center based on what the bot played
    __num_known_center_cards=[]

    #variable of played cards to explain how far the game has progressed
    num_played_cards = 0


    def __init__():
        pass

    """
    Constructor for a GameState requires:
    How many players, num_players, are playing
    The bot's hand, bot_hand
    Which player number is the bot, bot_player_number
    """
    def __init__(num_players,bot_hand,bot_player_number):
        for i in range(num_players):
            if i==bot_player_number:
                x=Player(bot_hand,calc_seq(i,num_players))
                __bot=x
            else:
                x=Player([],calc_seq(i,num_players))
            __players.append(x)
            

    """
    Calculates the sequence of cards to be played by a single player,
    based on the player number and how many players there are total.
    Assumes the game is using a full deck of 13 values.
    """
    def calc_seq(player_num,total_players):
        i = player_num
        seq=[]
        for x in range(13):
            if i>13:
                i=i%13
            if i==11:
                seq.append("J")
            elif i==12:
                seq.append("Q")
            elif i==13:
                seq.append("K")
            else:
                seq.append(i)
            i+=total_players
        return seq

    

class Player:

    #Represents the player's hand
    #For opponents, this shall be only cards the bot knows.
    __hand=[]

    #Represents the number of each card a player is holding.
    #This, while not necessary, makes calculating odds much easier
    #as you do not have to count the number of cards every time.
    #For opponents, this shall be only cards the bot knows.
    __num_each_card=[]

    #The number of cards in total
    __num_cards=0

    #The unique sequence for every player
    #in which they must play cards
    __sequence=[]

    #How many cycles it will take for the player to win.
    #For the bot, this can be calculated
    #though for the opponents, the lowest amount of cycles
    #will be assumed, ie, divide the number of cards they have
    #by 4 since they can play max 4 cards per turn.
    __cycles_until_win=0

    def __init__():
        pass

    """
    Constructor for a player requires:
    The player's hand, hand
    The player's sequence, sequence
    The rest of the properties (fields for Java ppl) can be calculated
    as they are in this constructor:
    num_cards=hand.len()
    Count the number of cards in __hand to get __num_each_card
    Find the last card in the sequence that the player has in hand, and
    the index of that card in sequence is how many turns until victory.
    """
    def __init__(hand,sequence):
        __hand=hand
        __sequence=sequence
        __num_cards=__hand.len()
        #TODO: are cards given sorted, or will we have to sort here?

        #Simply makes __num_each_card a list of 13 0s to add onto later
        for i in range(13):
            __num_each_card.append(0)
            
        for card in __hand:
            __num_each_card[card.get_val()]+=1
            #check this get_val() function in card class??
        for i in range(__sequence.len()-1,0,-1):
            for j in range(__hand):
                if __sequence[i]==__hand[j].get_val():
                    #same for here: check get_val()
                    __cycles_until_win=i
                break
            break
