from pgss import bluff, call_bluff, game_state

def run_bot():

    #Decision - put these variables in game_state,
    #or keep them here?
    bluff_thresh=.3 #temp
    call_thresh=.3 #temp
    in_progress=True
    
    game_state = game_state.GameState()
    bluff=bluff.BluffCalculator()
    call_bluff = call_bluff.CallBluffCalculator()
    start_game()
    while in_progress==True:
        #start playing the game here
"""
        if turn==self:
            play(self_turn(number,bluff_thresh))
            #where number is the number that we are being required to play.
            #can be calculated from sequence number or be pulled from the main
            #framework.
            #And play is supposedly a method to communicate to the server
            #to play a card.
"""
        pass

#starts the game and initializes the variables within game_state.
def start_game():
    #make calls to methods in game_state to initialize variables here
    pass

def self_turn(bluff_thresh):
    if decide_bluff!=False:
        #play selected cards
    else:
        #play cards

#TODO: clean up this method when the game_state variables are finished
#Decides which cards to play.
#Considers whether or not to lie by calling decide_bluff.
#Returns a list of cards to play.
def decide_cards_to_play(number,bluff_thresh):
    cards_to_play=[]
    if game_state.num_cards_self[number]!=0:
        cards_to_play.append(number)
        if decide_bluff(bluff_thresh)!=False:
            cards_to_play.append(bluff_card)
        return cards_to_play
    else:
        #TODO: find last owned card(s) in the sequence, and return that.

#Uses bluff.py to determine whether or not to lie.
#If the bot decides to lie, it returns the card to lie with.
#Otherwise, returns False.
def decide_bluff(bluff_thresh):
    if bluff.should_bluff() > bluff_thresh:
        bluff_card = bluff.pick_card_to_lie_with
        return bluff_card
    else:
        return False

#Uses call_bluff to determine whether or not to call bluff on an opponent.
#Returns True if the bot decides to lie. Otherwise, returns False.
def opponent_turn(opp,call_thresh):
    if call_bluff.should_call_bluff(game_state,opp)>call_thresh:
        return True
    else:
        return False

#Updates the various variables in game_state.
#This is called whenever the center pile is collected,
#ie, when someone calls bluff.
def center_pile_collected(player):
    pass

if __name__ == '__main__':
    run_bot()
    
