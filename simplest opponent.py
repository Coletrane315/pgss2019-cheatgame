from pgss import bluff, call_bluff, game_state
import cheat
from cheat import client
import time
import random

def run_bot():


    in_progress=False
    load_time=True #initial load time for the game
    c=cheat.client.Client("Simplest_Opponent")

    c.create_game()
    x = c.list_games()
    dictionary = x[-1]
    game_id = (dictionary['Id'])
    print(game_id)

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

        state = c.get_current_turn() #dictionary file with current turn info

        
        if load_time==True:
            time.sleep(1)
            load_time=False


        print(state)
        
        if int(state['Position']) == c.position:
            next_turn=state['Position']
            x=random.randint(0,len(c.hand)-1)
            c.update_player_info()
            time.sleep(1)
            c.play_cards(c.hand[1:3])
            time.sleep(1)
            c.update_player_info()
            print(c.hand)
            while(next_turn == state['Position']): #will essentially sleep the bot until the next turn
                time.sleep(1)
                state = c.get_current_turn()
            
        elif int(state['Position'])!= c.position:
            next_turn=state['Position']
            c.play_pass()
            time.sleep(0.1)
            c.update_player_info()
            while(next_turn == state['Position']):#will essentially sleep the bot until the next turn
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
def start_game(client):
    c=client
    c.start_game()
    info=c.get_current_turn()
    c.hand.sort(key=lambda x:x['Value'])


    


if __name__ == '__main__':
    run_bot()
    
