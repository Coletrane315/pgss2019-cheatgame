from pgss import probfunc
from pgss import game_state


class BluffCalculator:
        def prob_calculator(self, card_turn, game_state, r):
                #n is the number of a certain card the bot doesn't have. If the turn is 2's and the bot has 1 2, then n=3.
                botHandSize = game_state._bot._num_cards
                opp_hands=[]
                for player in game_state._players:
                        opp_hands.append(player._num_cards)
                opp_hands.remove(botHandSize)
                cards = game_state._bot._num_each_card
                chance_numerator = 0
                
                #Card_turn is value of card. 
                n = 4 - cards[card_turn - 1]
                for hand in opp_hands:
                        #"hand" stands for the number of cards the opponent has
                        # and "botHandSize" is the number of cards the bot has.
                        #I'm defining r as the number of cards of the desired value any opponent has in their hand.
                        #For clarity, n = 4-k for anyone looking at the formula in the paper. 
                        #Like, if you want to use this function to calculate the probability of an opponent having two Aces
                        #r = 2.
                        chance_numerator += probfunc.ncr(48-botHandSize+(4-n), hand - r)*probfunc.ncr(n, r)
                chance = 1- chance_numerator/ probfunc.ncr(52-botHandSize, hand)
                return chance           
        #precondition: we have x number of cards and need to find out if we should lie or not 
        #postcondition: returns the card that we should lie with (0 means we shouldn't lie)
        
        def should_bluff(self,game_state, card_turn, threshold):
                cards = game_state._bot._num_each_card
        
                #How many of card bot has. For people looking at formula on paper, num = k.     
                num = cards[card_turn - 1]
                if num == 0:
                        return self.should_bluff_0_card(card_turn, game_state, threshold)
                elif num == 1:
                        return self.should_bluff_1_card(card_turn, game_state, threshold) #kicks it to function to calculate when we have 1 card

                elif num == 2: 
                        return self.should_bluff_2_card(card_turn, game_state, threshold) #kicks it to function to calculate when we have 2 cards

                else:
                        return 0; #indicates we should not lie -- in this instance if we have 3 or 4 of a card
        
         #calculates whether we should lie if we have one card by calculating probability of opponent having 2 copies.
        def should_bluff_0_card(self, card_turn, game_state, threshold):
                cardsOfLastSeq = this.get_num_cards_of_last_seq(game_state)
                while cardsOfLastSeq > 1:    
                        value = self.prob_calculator(card_turn, game_state, cardsOfLastSeq)
                        if value > threshold:
                                return pick_card_to_lie_with(game_state, cardsOfLastSeq) #kicks it to figure out what we should lie with
                else:
                            cardsOfLastSeq -= 1 #we shouldn't lie because there is a high chance opponents will have card(s).
                return self.pick_card_to_lie_with(game_state, 1)
             
        #calculates whether we should lie if we have one card by calculating probability of opponent having 2 copies.
        def should_bluff_1_card(self, card_turn, game_state, threshold):
                valueLieWithThreeCopies = self.prob_calculator(card_turn, game_state, 2)
                valueLieWithTwoCopies = self.prob_calculator(card_turn, game_state, 3)
                if valueLieWithThreeCopies > threshold:
                        return self.pick_card_to_lie_with(game_state, 2) #kicks it to figure out what we should lie with
                elif valueLieWithTwoCopies > threshold:
                        return self.pick_card_to_lie_with(game_state, 1)
                else:
                        return 0 #we shouldn't lie because there is a high chance opponents will have card(s).
         
        
        #calculates whether we should lie if we have two cards by calculating probability of opponent having other 2 copies.       
        def should_bluff_2_card(self, card_turn, game_state, threshold):
                value = self.prob_calculator(card_turn, game_state, 2)
                if value > threshold:
                        return self.pick_card_to_lie_with(game_state, 2) #kicks it to figure out what we should lie with
                else:
                        return 0 #indicates we should not lie -- in this instance if we have 3 or 4 of a card
            
        #returns what card we should lie with
        def pick_card_to_lie_with(self, game_state, index):
                
                #x is the list of cards we lie with.    
                x = []    
                for i in range(0,index):
                        x.append(game_state._bot.get_last_card_in_seq())
                return x

        #returns the number of cards of the last value in sequence
        def get_num_cards_of_last_seq(self,game_state):
                count=0
                for i in range(len(self._sequence)-1,0,-1):
                        for j in range(len(self._hand)):
                                if self._sequence[i]==self.get_number_val(self._hand[j]['Value']):
                                        count+=1
                        if count!=0:
                                return count
                                        
