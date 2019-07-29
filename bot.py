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
            game_state.__bot.__sequence.append(game_state.__bot.__sequence.pop(0))
            c.update_player_info()
            #where value is the value that we are being required to play.
            #can be calculated from sequence number or be pulled from
            #a variable in the main framework.
"""
"""
Psuedocode for opponent turn:
        if turn!=self:
            if decide_call_bluff(call_thresh):
                c.play_call()
                c.update_player_info()
            else:
                c.play_pass()
                c.update_player_info()
"""
        pass

"""
Starts the game and initializes the variables within game_state.
"""
def start_game(game_state):
    pass
#starts the game and initializes the variables within game_state.
#TODO

"""
Decides which cards to play.
Considers whether or not to lie by calling decide_bluff.
Returns a list of cards to play.
"""
def decide_cards_to_play(value,bluff_thresh):
    bot=game_state.__bot
    cards_to_play=[]
    if bot.__num_each_card[bot.get_number_val(value)]!=0:
        for i in bot.__hand:
            if i.value==value:
                bot.__num_each_card[i.value-1]-=1
                cards_to_play.append(bot.__hand.remove(i))

        bluff_card=decide_bluff(bluff_thresh)
        if bluff_card!=False:
            for i in bot.__hand:
                if i==bluff_card:
                    bot.__num_each_card[i.value-1]-=1
                    cards_to_play.append(bot.__hand.remove(i))
        return cards_to_play
    else:
        return bot.get_last_card_in_seq()
    
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
def decide_call_bluff(opp,call_thresh,card_val,num_cards_played):
    if call_bluff.should_call_bluff(game_state,opp,card_val,num_cards_played)>=call_thresh:
        return True
    else:
        return False

"""
Updates the various variables in game_state.
This is called whenever the center pile is collected,
ie, when someone calls bluff.
"""
def center_pile_collected(game_state,player_num):
    for card in game_state.__known_center_cards:
        game_state.__players[player_num].__hand.append(game_state.__known_center_cards.pop(card))
    game_state.__num_played_cards+=game_state.__num_cards_center
    game_state.__num_cards_center=0
    #TODO: this looks good but I feel like something is missing.

if __name__ == '__main__':
    run_bot()
    
