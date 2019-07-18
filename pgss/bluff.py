class BluffCalculator:

        #precondition: we have x number of cards and need to find out if we should lie or not 
        #postcondition: returns the card that we should lie with (0 means we shouldn't lie)
        def should_bluff(self,game_state):
            cards = random.randint(0,4) 
            if cards is 0: 
                  return pick_card_to_lie_with(self, game_state) #goes straight to picking a card since we have to lie

            elif cards is 1:
                return should_bluff_1_card(self, game_state) #kicks it to function to calculate when we have 1 card

            elif cards is 2: 
                return should_bluff_2_card(self, game_state) #kicks it to function to calculate when we have 2 cards

            else:
                return 0; #indicates we should not lie -- in this instance if we have 3 or 4 of a card

        #calculates whether we should lie if we have one card
        def should_bluff_1_card(self, game_state):
            value = 'something'
            if value is 'good': 
                return pick_card_to_lie_with #kicks it to figure out what we should lie with
            
            else:
                return 0; #we shouldn't lie

        #calculates whether we should lie if we have two cards       
        def should_bluff_2_card(self, game_state):
            value = 'something'
            if value is 'good': 
                return pick_card_to_lie_with #kicks it to figure out what we should lie with
            
            else:
                return 0; #we shouldn't lie
            
        #returns what card we should lie with
        def pick_card_to_lie_with(self, game_state):
            x = 5 #temp 
            return x; 
