from pgss import bluff, call_bluff, game_state
import cheat
from cheat import client

def run_bot():

    game_id='fc8d5b21-223b-4e7e-afee-8b1996356299'
    #CHANGE GAME ID TO MATCH THE ONE YOU WANT TO JOIN

    bluff_thresh=.3 #temp
    call_thresh=.3 #temp
    in_progress=False
    c=cheat.client.Client("My_Cheat_Bot")

    join_game(c,game_id)
    #wait for the game to start
    while in_progress==False:
        x=c.get_current_turn()
        if x!=None:
            in_progress=True
        else:
            in_progress=False
    
    game_state=start_game(c)
    current_turn={'Id':0}
    
    while in_progress==True:
        #start playing the game here
#        c.update_game()
        c.update_player_info()
        
        if current_turn['Id']!=c.get_current_turn()['Id']:
            current_turn=c.get_current_turn()
            print("time to play!")
            if int(current_turn['Position'])==game_state._bot_pos:
                print("playing cards...")
                value=c.get_current_turn()['CardValue']
                c.play_cards(decide_cards_to_play(value,game_state,bluff_thresh))
                game_state._bot._sequence.append(game_state._bot._sequence.pop(0))
                c.update_player_info()

        try:
            if int(c.get_current_turn()['Position'])!=game_state._bot_pos and c.get_current_turn()['CardsDown']!=0:
                print("deciding to call...")
                x=c.get_current_turn()
                if decide_call_bluff(game_state,x['Position'],x['CardValue'],x['CardsDown'],call_thresh):
                    print("i call cheat!")
                    c.play_call()
                    c.update_player_info()
                else:
                    print("seems ok enough...")
                    c.play_pass()
                    c.update_player_info()
        except KeyError:
            #this is basically just for the case where the ['CardsDown'] key
            #isn't in the turn dictionary, so nothing happens since
            #you can't call cheat on nothing.
            pass
            
"""
Joins the game.
"""
def join_game(client,game_id):
    client.game_id=game_id
    client.join_game()
    client.update_game()
    client.update_player_info()

"""
Starts the game and initializes the variables within game_state.
"""
def start_game(client):
    client.update_game()
    client.update_player_info()
    client.hand.sort(key=lambda x:x['Value'])
    print("hand: "+str(c.hand))
    gs=game_state.GameState(c.players_connected,c.hand,int(c.position))
    return gs
    

"""
Decides which cards to play.
Considers whether or not to lie by calling decide_bluff.
Returns a list of cards to play.
"""
def decide_cards_to_play(value,game_state,bluff_thresh):
    print("hand on local: "+str(game_state._bot._hand))
    bot=game_state._bot
    value=bot.get_number_val(value)
    cards_to_play=[]
    if bot._num_each_card[value-1]!=0:
        for i in range(len(bot._hand)):
            if bot._hand[i]['Value']==value:
                bot._num_each_card[bot._hand[i]['Value']-1]-=1
                cards_to_play.append(bot._hand[i])
        bot._cycles_until_win-=1

        bluff_card=decide_bluff(bluff_thresh,game_state,value)
        if bluff_card!=False:
            bot.__cycles_until_win-=1
            for i in range(len(bot._hand)):
                if bot._hand[i]==bluff_card:
                    bot._num_each_card[bot._hand[i]['Value']-1]-=1
                    cards_to_play.append(bot._hand[i])

        for i in cards_to_play:
            bot._hand.remove(i)
            game_state._known_center_cards.append(i)
        game_state._num_cards_center+=len(cards_to_play)
                    
        print("cards played (truth): "+str(cards_to_play))
        return cards_to_play
    
    else:
        print("card played (forced to lie: "+str(bot.get_last_card_in_seq()))
        x=bot.get_last_card_in_seq()
        cards_to_play.append(x)
        bot._hand.remove(x)
        game_state._known_center_cards.append(x)
        game_state._num_cards_center+=len(cards_to_play)
        return cards_to_play
    
"""
Uses bluff.py to determine whether or not to lie.
If the bot decides to lie, it returns the card to lie with.
Otherwise, returns False.
"""
def decide_bluff(bluff_thresh,game_state,card_val):
    bluff_calc=bluff.BluffCalculator()
    print(bluff_calc.should_bluff(game_state,game_state.get_number_val(card_val)))
    if bluff_calc.should_bluff(game_state,game_state.get_number_val(card_val)) > bluff_thresh:
        bluff_card = bluff_calc.pick_card_to_lie_with(game_state)
        return bluff_card
    else:
        return False

"""
Uses call_bluff to determine whether or not to call bluff on an opponent.
Returns True if the bot decides to lie. Otherwise, returns False.
"""
def decide_call_bluff(game_state,opp,card_val,num_cards_played,call_thresh):
    call_bluff_calc = call_bluff.CallBluffCalculator()
    if call_bluff_calc.should_call_bluff(game_state,opp,card_val,num_cards_played)>=call_thresh:
        return True
    else:
        return False

"""
Updates the various variables in game_state.
This is called whenever the center pile is collected,
ie, when someone calls bluff.
"""
def center_pile_collected(game_state,player_num):
    print("i know that player "+str(player_num)+" has "+str(game_state._known_center_cards))
    for card in game_state._known_center_cards:
        game_state._players[player_num]._hand.append(game_state._known_center_cards.pop(card))
    game_state._players[player_num].hand.sort(key=lambda x:x['Value'])
    game_state._players[player_num].update()
    game_state._num_played_cards+=game_state.__num_cards_center
    game_state._num_cards_center=0
    if game_state._players[player_num]==game_state._bot:
        game_state._bot.count_cycles_until_win_bot()
    #TODO: this looks good but I feel like something is missing.

if __name__ == '__main__':
    run_bot()
    
