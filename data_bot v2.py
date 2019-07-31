from pgss import bluff, call_bluff, game_state
import cheat
from cheat import client
import csv
import time


def run_bot():
    with open('data.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        
        bluff_thresh=.3 #temp
        call_thresh=.3 #temp
        in_progress=False
        c=cheat.client.Client("My_Cheat_Bot")
        c.create_game(4)
        game_list = c.list_games()
        game_id= game_list[-1]['Id']
        join_game(c,game_id)

        while c.players_connected != 4:
            c.update_game()
            time.sleep(1)
        c.start_game()
        
        if c.wait_for_message()[0]=='GAME_STARTED':
            game_state=start_game(c)
        
        while True:
            #start playing the game here
            c.update_player_info()
            lie = []
            
            print("time to play!")
            game_state._bot._hand = c.hand
            
            if int(c.get_current_turn()['Position'])==game_state._bot_pos:
                data = []
                data.append(len(c.hand))
                
                print("playing cards...")
                value=c.get_current_turn()['CardValue']
                c.play_cards(decide_cards_to_play(value,game_state,bluff_thresh,data,lie))
                game_state._bot._sequence.append(game_state._bot._sequence.pop(0))
                c.update_player_info()
                c.hand.sort(key=lambda x:x['Value'])
                game_state._bot._hand=c.hand
                game_state._bot.count_num_cards
                game_state._bot.count_cycles_until_win_bot()
                msg=c.wait_for_message()
                if msg[0]=='GAME_OVER':
                    break

            else:
                msg=c.wait_for_message()
                if msg[0]=='GAME_OVER':
                    print('Gave Over')
                    break
                
                if  msg[0]=='CARDS_PLAYED':
                    x=c.get_current_turn()

                    game_state._players[int(x['Position'])-1]._cards_played_into_center+=int(x['CardsDown'])
                    game_state._players[int(x['Position'])-1]._sequence.append(game_state._players[int(x['Position'])-1]._sequence[-1])
                    
                    #remove known cards from opponent
                    if game_state._players[int(x['Position'])-1]._num_cards!=0:
                        if game_state._players[int(x['Position'])-1]._num_each_card[game_state.get_number_val(x['CardValue'])-1]!=0:
                            for card in game_state._players[int(x['Position'])-1]._hand:
                                if game_state.get_number_val(card['Value'])==game_state.get_number_val(x['CardValue']):
                                    game_state._players[int(x['Position'])-1]._hand.remove(card)
                                    game_state._players[int(x['Position'])-1]._num_cards-=1
                            game_state._players[int(x['Position'])-1]._num_each_card[game_state.get_number_val(x['CardValue'])-1]=0 

                    print("deciding to call...")

                    if decide_call_bluff(game_state,x['Position'],x['CardValue'],x['CardsDown'],call_thresh):
                        print("i call cheat!")
                        c.play_call()
                        c.update_player_info()
                    else:
                        print("seems ok enough...")
                        c.play_pass()
                        c.update_player_info()

                
            msg=c.wait_for_message()
            called = 1
            
            if msg[0]=='CALLED':
                if msg[1][1]['WasLie']==False:
                    center_pile_collected(game_state,int(msg[1][1]['CallPosition']),msg[1][1]['Cards'],c)
                else:
                    x=c.get_current_turn()
                    center_pile_collected(game_state,int(x['Position']),msg[1][1]['Cards'],c)
                msg=c.wait_for_message()

            if(len(lie) != 0):
                data.append(called)
                writer.writerow(data)
            if msg[0]=='GAME_OVER':
                print('Gave Over')
                break
            if msg[0]=='TURN_OVER':
                pass

        csvFile.close()





"""
Joins the game.
"""
def join_game(client,game_id):
    client.game_id=game_id
    client.join_game()
    client.update_player_info()
    client.update_game()

"""
Starts the game and initializes the variables within game_state.
"""
def start_game(client):
    client.update_game()
    client.update_player_info()
    client.hand.sort(key=lambda x:x['Value'])
    gs=game_state.GameState(client.players_connected,client.hand,int(client.position)-1)
    return gs
    

"""
Decides which cards to play.
Considers whether or not to lie by calling decide_bluff.
Returns a list of cards to play.
"""
def decide_cards_to_play(value,game_state,bluff_thresh,data,lie):
    print("hand on local: "+str(game_state._bot._hand))
    bot=game_state._bot
    value=bot.get_number_val(value)
    cards_to_play=[]
    bluff_calc=bluff.BluffCalculator()
    cards=bluff_calc.should_bluff(game_state,value,bluff_thresh)
    if cards!=0:
        lie.append(0)
        cards_to_play=cards
        data.append(game_state._num_cards_center)
        data.append(game_state._num_played_cards)
        num_r = 0
        for c in cards:
            if c['Value'] == value:
                num_r += 1
        data.append(bluff_calc.prob_calculator(value,game_state,5-num_r))

    for card in bot._hand:
        if card['Value']==value:
            cards_to_play.append(card)
    game_state._num_cards_center+=len(cards_to_play)

    bot._cards_played_into_center+=len(cards_to_play)

    for card in cards_to_play:
        game_state._known_center_cards.append(card)
    
    print("cards played: " + str(cards_to_play))
    return cards_to_play
    

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
def center_pile_collected(game_state,player_num,turned_cards,c):
    player_index=int(player_num)-1
    print("i know that player "+str(player_num)+" has "+str(game_state._known_center_cards))
    have_card=False
    for card in turned_cards:
        have_card=False
        for known_card in game_state._players[player_index]._hand:
            if card==known_card:
                have_card=True
        if have_card==False:
            game_state._players[player_index]._hand.append(card)
    for card in game_state._known_center_cards:
        have_card=False
        for known_card in game_state._players[player_index]._hand:
            if card==known_card:
                have_card=True
        if have_card==False:
            game_state._players[player_index]._hand.append(card)
    game_state._players[player_index]._hand.sort(key=lambda x:game_state.get_number_val(x['Value']))
    game_state._players[player_index].count_num_cards()
    game_state._players[player_index]._num_cards+=(game_state._num_cards_center+len(turned_cards))
    game_state._num_played_cards+=game_state._num_cards_center
    game_state._num_cards_center=0
    game_state._num_played_cards-=game_state._players[player_index]._cards_played_into_center
    if game_state._players[player_index]==game_state._bot:
        c.update_player_info()
        game_state._bot._hand=c.hand
        game_state._bot._hand.sort(key=lambda x:game_state.get_number_val(x['Value']))
        game_state._bot.count_num_cards()
        game_state._bot.count_cycles_until_win_bot()
    for player in game_state._players:
        player._cards_played_into_center=0

if __name__ == '__main__':
    while True:
        run_bot()
    
