class Player:

    #Represents the player's hand
    #For opponents, this shall be only cards the bot knows.
    _hand:[]

    #Represents the number of each card a player is holding.
    #This, while not necessary, makes calculating odds much easier
    #as you do not have to count the number of cards every time.
    #For opponents, this shall be only cards the bot knows.
    _num_each_card:[]

    #The number of cards in total in the player's hand.
    #This is known for the opponents too based on what they played.
    _num_cards:0

    #The unique sequence for every player
    #in which they must play cards
    _sequence:[]

    #How many cycles it will take for the player to win.
    #For the bot, this can be calculated
    #though for the opponents, the lowest amount of cycles
    #will be assumed, ie, divide the number of cards they have
    #by 4 since they can play max 4 cards per turn.
    _cycles_until_win:0

    #How many cards this player has played into the center pile.
    #Resets when the center pile is collected.
    #Used for tracking cards that switched hands.
    _cards_played_into_center:0

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
    def __init__(self,hand,sequence):
        self._hand=hand
        self._sequence=sequence
        self._num_cards=len(self._hand)
        self._num_each_card=[]
        self._num_cards=0
        self._cycles_until_win=0
        
        #TODO: are cards given sorted, or will we have to sort here?

        #Simply makes __num_each_card a list of 13 0s to add onto later
        for i in range(13):
            self._num_each_card.append(0)
            
        self.count_num_cards()
        self.count_cycles_until_win()

    def update(self):
        self.count_num_cards()
        self.count_cycles_until_win()

    def count_num_cards(self):
        for card in self._hand:
            if isinstance(card,dict):
                self._num_each_card[card['Value']-1]+=1

    def count_cycles_until_win_bot(self):
        for i in range(len(self._sequence)-1,0,-1):
            for j in range(len(self._hand)):
                if self._sequence[i]==self._hand[j]['Value']:
                    self._cycles_until_win=i
                break
            break

    def count_cycles_until_win(self):
        self._cycles=len(self._hand)/4

    def get_last_card_in_seq(self):
        for i in range(len(self._sequence)-1,0,-1):
            for j in range(len(self._hand)):
                if self._sequence[i]==self.get_number_val(self._hand[j]['Value']):
                    self._num_each_card[self.get_number_val(self._hand[j]['Value'])-1]-=1
                    return self._hand.pop(j)
                
    def get_number_val(self,card_val):
        if isinstance(card_val,list):
            card_val=card_val[1]
        if card_val=="Ace":
            return 1
        elif card_val=="Jack":
            return 11
        elif card_val=="Queen":
            return 12
        elif card_val=="King":
            return 13
        return int(card_val)

class GameState:

    #list of player objects representing players in the game
    _players:[]

    #player object which is the bot, also represented in __players
    _bot:Player([],[])

    #position of the bot
    _bot_pos:0

    #the number of cards in the center pile
    _num_cards_center:0

    #the known cards in the center based on what the bot played
    _known_center_cards:[]

    #variable of played cards to explain how far the game has progressed
    _num_played_cards:0

    def __init__():
        pass

    """
    Constructor for a GameState requires:
    How many players, num_players, are playing
    The bot's hand, bot_hand
    Which player number is the bot, bot_player_number
    """
    def __init__(self,num_players,bot_hand,bot_player_number):
        self._players=[]
        self._bot_pos=bot_player_number
        self._num_cards_center=0
        self._known_center_cards=[]
        self._num_played_cards=0
        for i in range(1,num_players+1):
            if i==bot_player_number:
                x=Player(bot_hand,self.calc_seq(i,num_players))
                self._bot=x
            else:
                x=Player([],self.calc_seq(i,num_players))
            self._players.append(x)
            

    """
    Calculates the sequence of cards to be played by a single player,
    based on the player number and how many players there are total.
    Assumes the game is using a full deck of 13 values.
    """
    def calc_seq(self,player_num,total_players):
        i = player_num
        seq=[]
        for x in range(13):
            if i>13:
                i=i%13
            seq.append(i)
            i+=total_players
        return seq

    def get_number_val(self,card_val):
        if isinstance(card_val,list):
            card_val=card_val[1]
        if card_val=="Ace":
            return 1
        elif card_val=="Jack":
            return 11
        elif card_val=="Queen":
            return 12
        elif card_val=="King":
            return 13
        return int(card_val)
