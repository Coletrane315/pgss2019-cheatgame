import cheat
from cheat import client
import time
import random

def run_bot():


    in_progress=True
    load_time=True #initial load time for the game
    name = 'bot' + str(random.randint(0,1000000))
    c=cheat.client.Client(name)
    x = c.list_games()
    dictionary = x[-1]
    game_id = (dictionary['Id'])
    c.game_id = game_id
    c.join_game()

    #wait for the game to start
    

    c.wait_for_message()
    
    while in_progress==True:
        #start playing the game here
        c.update_game()
        c.update_player_info()
        c.hand.sort(key=lambda x:x['Value'])

        state = c.get_current_turn() #dictionary file with current turn info
        print(state)
        
        if load_time==True:
            time.sleep(1)
            load_time=False

        #print(state)
        
        if int(state['Position']) == c.position:
            c.update_player_info()
            
            y = random.randint(1,4)
            x=random.randint(0,len(c.hand)-1)
            while x+y>len(c.hand):
                if(x>0):
                    x-=1
                y-=1
            time.sleep(1)
            c.play_cards(c.hand[x:x+y])
            
            time.sleep(1)
            c.update_player_info()
            #print(c.hand)

            message = c.wait_for_message()
            if(message[0] == 'GAME_OVER'):
                return
            message = c.wait_for_message()
            if(message[0] == 'CALLED'):
                message = c.wait_for_message()
            
                
        elif int(state['Position'])!= c.position:
            c.wait_for_message()
            time.sleep(0.5)
            x=random.randint(0,1)
            if x == 0:
                c.play_pass()
            else:
                c.play_call()
            time.sleep(0.1)
            c.update_player_info()
            message = c.wait_for_message()
            if(message[0] == 'GAME_OVER'):
                return
            if(message[0] == 'CALLED'):
                message = c.wait_for_message()

        time.sleep(1)
            
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
    info=c.get_current_turn()
    c.update_player_info()
    c.hand.sort(key=lambda x:x['Value'])


    


if __name__ == '__main__':
    run_bot()
    
