from pgss import bluff, call_bluff, game_state
import cheat.client

def run_bot():

    bluff_thresh=.3 #temp
    call_thresh=.3 #temp
    in_progress=True
    c=cheat.client.Client("My_Bot")
    
    game_state = game_state.GameState()
    bluff=bluff.BluffCalculator()
    call_bluff = call_bluff.CallBluffCalculator()
    
    start_game(game_state)
    while in_progress==True:
        #start playing the game here
"""
Psuedocode for self turn:
        if turn==self:
            c.play_cards(decide_card_to_play(value,bluff_thresh))
            #where value is the value that we are being required to play.
            #can be calculated from sequence number or be pulled from
            #a variable in the main framework.
"""
"""
Psuedocode for opponent turn:
        if turn!=self:
            if decide_call_bluff(call_thresh):
                c.play_call()
            else:
                c.play_pass()
"""
        pass

"""
Starts the game and initializes the variables within game_state.
"""
def start_game(game_state):
    pass
#starts the game and initializes the variables within game_state.
#TODO

#TODO: clean up this method when the game_state variables are finished
        #consider cards_self for the list of cards that the bot holds
        #consider num_of_cards for the list of how many of each card the bot holds
        #Don't worry if your vars don't line up - I can clean it up to fit with
        #yours later --Frank
"""
Decides which cards to play.
Considers whether or not to lie by calling decide_bluff.
Returns a list of cards to play.
"""
def decide_cards_to_play(value,bluff_thresh):
    cards_to_play=[]
    if game_state.num_of_cards[value]!=0:
        for i in cards_self:
            if i.value==number:
                cards_to_play.append(cards_self.pop(i))
        num_of_cards=0

        bluff_card=decide_bluff(bluff_thresh)
        if bluff_card!=False:
            for i in cards_self:
                if i==bluff_card:
                    cards_to_play.append(cards_self.pop(i))
        return cards_to_play
    else:
        #TODO: find last owned card(s) in the sequence, and return that.

"""
Uses bluff.py to determine whether or not to lie.
If the bot decides to lie, it returns the card to lie with.
Otherwise, returns False.
"""
def decide_bluff(bluff_thresh):
    if bluff.should_bluff() > bluff_thresh:
        bluff_card = bluff.pick_card_to_lie_with(game_state)
        return bluff_card
    else:
        return False

"""
Uses call_bluff to determine whether or not to call bluff on an opponent.
Returns True if the bot decides to lie. Otherwise, returns False.
"""
def decide_call_bluff(opp,call_thresh):
    if call_bluff.should_call_bluff(game_state,opp)>=call_thresh:
        return True
    else:
        return False

"""
Updates the various variables in game_state.
This is called whenever the center pile is collected,
ie, when someone calls bluff.
"""
def center_pile_collected(player):
    #TODO: make calls to game_state to update variables
    pass

if __name__ == '__main__':
    run_bot()
    
