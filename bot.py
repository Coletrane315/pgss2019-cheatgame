from pgss import bluff, call_bluff, game_state, probfunc.py, sequence.py

def run_bot():
    game_state = game_state.GameState()
    bluff=bluff.BluffCalculator()
    call_bluff = call_bluff.CallBluffCalculator()
    start_game()
#    while game_state.in_progress==True:

#starts the game and initializes the variables within game_state.
def start_game():
    pass

#Uses bluff.py to determine whether or not to lie.
#If the bot decides to lie, it returns the card to lie with.
#Otherwise, returns False.
def self_turn(bluff_thresh):
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

def center_pile_collected(player):
    pass

if __name__ == '__main__':
    run_bot()
    
