from pgss import bluff, call_bluff, game_state
import cheat
from cheat import client
import time
import random

def run_bot():

    
    bluff_thresh=.3 #temp
    call_thresh=.3 #temp
    in_progress=False
    load_time=True
    c=cheat.client.Client("Human_Interface")

    x = c.list_games()
    game_id = input("Input Game ID please: ")

    join_game(c,game_id)
    #wait for the game to start
    while in_progress==False:
        x=input("Start the game? y/n ")
        if x == "y":
            in_progress=True
        else:
            in_progress=False

    
    while in_progress==True:
        #start playing the game here
        c.update_game()
        c.update_player_info()

        state = c.get_current_turn()

        
        if load_time==True:
            time.sleep(1)
            load_time=False


        print(state)
        
        if int(state['Position']) == c.position:
            next_turn=state['Position']
            c.update_player_info()
            time.sleep(1)
            x = input("What cards would you like to play?: ")
            time.sleep(1)
            c.update_player_info()
            print(c.hand)
            while(next_turn == state['Position']):
                time.sleep(1)
                state = c.get_current_turn()
            
        elif int(state['Position'])!= c.position:
            next_turn=state['Position']
            c.play_pass()
            time.sleep(0.1)
            c.update_player_info()
            while(next_turn == state['Position']):
                time.sleep(1)
                state = c.get_current_turn()

        time.sleep(0.5)
            
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

    


if __name__ == '__main__':
    run_bot()
    
