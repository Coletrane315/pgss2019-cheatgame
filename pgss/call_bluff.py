from pgss import game_state
from pgss import probfunc
import math

class CallBluffCalculator:
    """
    Determines whether the bot should call bluff or not.
    Returning a value of 1.0 means it is guaranteed to call bluff.
    Otherwise, returns a float indicating the probability that it should
    call bluff.
    This float is used in bot.py by comparison against a threshold to ultimately
    tell the bot if it should call or not.
    """
    def should_call_bluff(self,game_state, opponent, card_val, num_cards_played):
        # decides whether or not the bot should call bluff on another player.
        if card_val=="Ace":
            card_val=1
        elif card_val=="Jack":
            card_val=11
        elif card_val=="Queen":
            card_val=12
        elif card_val=="King":
            card_val=13
        if isinstance(card_val,list):
            card_val=int(card_val[1])
        opponent_ind=int(opponent)-1
        print(str(game_state._bot._num_each_card))
        k = game_state._bot._num_each_card[card_val-1] #should be the number of the sought card in own hand
        r = num_cards_played #should be the number of the sought card played by the opponent
        h = game_state._bot._num_cards #should be own hand size
        l = game_state._players[opponent_ind]._num_cards #should be opponent's hand size
        j = game_state._bot._cycles_until_win #should be how many turns until bot wins
        i = game_state._num_cards_center+num_cards_played #should be number of cards in center pile

        print(str(h)+" "+str(l))

        for card in game_state._known_center_cards:
            if game_state.get_number_val(card['Value'])==card_val:
                k+=1

        for card in game_state._known_center_cards:
            for hand in game_state._bot._hand:
                if (game_state.get_number_val(card['Value']) == game_state.get_number_val(hand['Value'])):
                    i-=1

	#immediately call bluff if it's the opponent's last card
        if (l==0):
            return 1.0

	#immediately call bluff if there appear to be more than four of a kind
        if (k+r > 4):
            return 1.0

	#otherwise, calculate the probability of the player lying
	#considers both the probability of the opponent not having the card
	#as well as how many cards are in the center pile (risk)
        #and how close the bot is to winning (it will not lie if it can win
        #in the next two turns), as it returns a negative float then.

        prob=probfunc.ncr(4-k,r)*probfunc.ncr(48-h+k,l-r)/probfunc.ncr(52-h,l)

        return  (1-prob)*(1/(i+1))*(0.001/(0.001+0.001*0.999*math.exp(-0.5*(h-6.5))))*(1/(h+1))
        #The giant function at the end represents a logistic growth function that
        #peaks at around 13 cards

