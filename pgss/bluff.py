from pgss import probfunc
from pgss import game_state


class BluffCalculator:
        def prob_calculator(self, card_turn, game_state, r):
                #A is the size of the bot's hand. B, C, and D are the hand sizes of players 2,3 and 4 respectively. n is the number of a
                #certain card the bot doesn't have. If the turn is 2's and the bot has 1 2, then n=3.
                botHandSize = game_state._bot._num_cards
                opp_hands=[]
                for player in game_state._players:
                        opp_hands.append(player._num_cards)
                opp_hands.remove(botHandSize)
                cards = game_state._bot.num_each_cards
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
                chance = chance_numerator/ probfunc.ncr(52-botHandSize, hand)
                return chance           
        #precondition: we have x number of cards and need to find out if we should lie or not 
        #postcondition: returns the card that we should lie with (0 means we shouldn't lie)
        
       def should_bluff(self,game_state, card_turn):
            cards = game_state._bot._num_each_card
        
            #How many of card bot has. For people looking at formula on paper, num = k.     
            num = cards[card_turn - 1]
            if num == 1:
                return should_bluff_1_card(game_state) #kicks it to function to calculate when we have 1 card

            elif num == 2: 
                return should_bluff_2_card(game_state) #kicks it to function to calculate when we have 2 cards

            else:
                return 1; #indicates we should not lie -- in this instance if we have 3 or 4 of a card

        #calculates whether we should lie if we have one card by calculating probability of opponent having 2 copies.
        def should_bluff_1_card(self, game_state):
            valueLieWithThreeCopies = prob_calculator(game_state, 2)
            valueLieWithTwoCopies = prob_calculator(game_state, 3)
            if value >= 0 and value <= 1:
                if valueLieWithThreeCopies < 0.5:
                        return pick_card_to_lie_with(game_state, 2) #kicks it to figure out what we should lie with
                elif valueLieWithTwoCopies < 0.5:
                        return pick_card_to_lie_with(game_state, 1)
                else:
                        return 1 #we shouldn't lie because there is a high chance opponents will have card(s).
'''
         #calculates whether we should lie if we have one card by calculating probability of opponent having 2 copies.
        def should_bluff_1_card(self, game_state):
            value = prob_calculator(game_state, 2)
            if value >= 0 and value <= 1:
                    if value > 0.5:
                            return pick_card_to_lie_with #kicks it to figure out what we should lie with
            
            else:
                return 0 #we shouldn't lie
                
        #calculates whether we should lie if we have one card by calculating probability of opponent having 3 copies.
        def should_bluff_1_card(self, game_state):
            value = prob_calculator(game_state, 3)
            if value >= 0 and value <= 1:
                    if value > 0.5:
                            return pick_card_to_lie_with #kicks it to figure out what we should lie with
            
            else:
                return 0 #we shouldn't lie
'''                
        
        #calculates whether we should lie if we have two cards by calculating probability of opponent having other 2 copies.       
        def should_bluff_2_card(self, game_state):
                value = prob_calculator(game_state, 2)
            #CHANGE 0.5 ONCE MACHINE LEARNING DONE
                if value >= 0 and value <= 1:
                        if value < 0.5:
                                return pick_card_to_lie_with(game_state, 2) #kicks it to figure out what we should lie with
            
                        else:
                                return 1 #indicates we should not lie -- in this instance if we have 3 or 4 of a card
            
        #returns what card we should lie with
        def pick_card_to_lie_with(self, game_state, index):
                
            #x is the list of cards we lie with.    
            x = []    
            for i in range(0,index)   
                x.append(game_state._bot.get_last_card_in_seq())
            return x 
