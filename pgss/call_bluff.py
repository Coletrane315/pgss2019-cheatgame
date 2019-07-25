import game_state

class CallBluffCalculator:

    def should_call_bluff(self,game_state, threshold, opponent, card_type_played, num_cards_played):
        # decides whether or not the bot should call bluff on another player.

	card_played = card_played
        k = self.__cards_of_player[0].count(card_played) #should be the number of the sought card in own hand
        r= num_cards_played #should be the number of the sought card played by the opponent
        h = self.__num_cards_hands[0] #should be own hand size
        l = self.__cards_of_hands[opponent] #should be opponent's hand size

	#immediately call bluff if it's the opponent's last card
        if (l==0):
            return True

	#immediately call bluff if there appear to be more than four of a kind
        if (k+r > 4):
            return True

	#otherwise, calculate the probability of the player lying
	#considers both the probability of the opponent not having the card
	#as well as how many cards are in the center pile (risk)

        prob=probfunc.ncr(4-k,r)*probfunc.ncr(48-h+k,l-r)/probfunc.ncr(52-h,l)

        return  (1-prob)*(1/self.cards_in_pile)

