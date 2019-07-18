class CallBluffCalculator:

    def should_call_bluff(self,game_state, threshold):
        # decides whether or not the bot should call bluff on another player.

	#immediately call bluff if it's the opponent's last card
	if (playing player has 0 cards):
		return True

	#immediately call bluff if there appear to be more than four of a kind
	if (num of cards in own hand + number of cards played > 4):
		return True

	#otherwise, calculate the probability of the player lying
	#considers both the probability of the opponent not having the card
	#as well as how many cards are in the center pile (risk)
	n=cards in own hand
	r=4-n
	p=players
	prob=r/p-1
	if ((1-prob)*(1/cards in center)>threshold):
		return  True
	return  False

