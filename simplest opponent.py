from pgss import bluff, call_bluff, game_state
import cheat
from cheat import client
import time
import random

def run_bot():

    
    bluff_thresh=.3 #temp
    call_thresh=.3 #temp
    in_progress=False
    c=cheat.client.Client("Simplest_Opponent")

    c.create_game()
    x = c.list_games()
    dictionary = x[-1]
    game_id = (dictionary['Id'])

    join_game(c,game_id)
    #wait for the game to start
    while in_progress==False:
        x=input("Start the game? y/n ")
        if x == "y":
            in_progress=True
        else:
            in_progress=False
    
    game_state=start_game(c)
    
    while in_progress==True:
        #start playing the game here
        c.update_game()
        c.update_player_info()
        time.sleep(1)

        state = c.get_current_turn()

        print(state)
        print(c.position)
                
        if state['Position']== c.position:
            x=random.randint(0,len(c.hand)-1)
            c.play_cards(c.hand[x:x+1])
            c.update_player_info()
            c.hand
            
        elif state['Position']!= c.position:
            c.play_pass()
            c.update_player_info()

        time.sleep(60)
            
"""
Joins the game.
"""
def join_game(client,game_id):
    c=client
    c.game_id=game_id
    c.join_game()
    c.update_game()
    c.update_player_info()

"""
Starts the game and initializes the variables within game_state.
"""
def start_game(client):
    c=client
    c.start_game()
    info=c.get_current_turn()
    c.hand.sort(key=lambda x:x['Value'])


    


if __name__ == '__main__':
    run_bot()
    
