import cheat
from cheat import client
import time
import random

def run_bot():

    in_progress=False
    load_time=True
    c=cheat.client.Client("Human_Interface")

    print(c.list_games())
    game_id = input("Input Game ID please: ")

    join_game(c,game_id)

    message = c.wait_for_message()


    
    while True:
        #start playing the game here
        c.update_game()
        c.update_player_info()
        hand.sort(key=lambda x:x['Value'])

        state = c.get_current_turn()

        
        if load_time==True:
            time.sleep(1)
            load_time=False

        
        if int(state['Position']) == c.position:
            next_turn=state['Position']
            c.update_player_info()
            c.hand.sort(key=lambda x:x['Value'])
            print(c.hand)

            x = []
            y = input("Which number are you playing? Enter -1 to stop choosing")
            for y != '-1':
                check == False
                for cards in c.hand:
                    if cards['Value'] == y:
                        x.append(cards)
                        check == True
                if !check:
                    print("Card not in hand")
                      
            c.play_cards(x)
            
            time.sleep(1)
            c.update_player_info()
            #print(c.hand)

            message = c.wait_for_message()
            if(message[0] == 'GAME_OVER'):
                print ("Game Over: Position: " + message['WinningPosition'] + " won!")
                return
            message = c.wait_for_message()
            if(message[0] == 'CALLED'):
                print("Somebody called bluff")
                if(message[1]['WasLie']):
                    print("It was a lie")
                else:
                    print("It was not a lie")
                message = c.wait_for_message()
                print("Turn Over")
            
        elif int(state['Position'])!= c.position:
            message = c.wait_for_message()

            x = input("Pass or 
            c.play_pass()
            time.sleep(0.1)
            c.update_player_info()
            while(next_turn == state['Position']):#will essentially sleep the bot until the next turn
                time.sleep(1)
                state = c.get_current_turn()
            message = c.wait_for_message()
            if(message[0] == 'GAME_OVER'):
                print ("Game Over: Position: " + message['WinningPosition'] + " won!")
                return
            if(message[0] == 'CALLED'):
                message = c.wait_for_message()

        time.sleep(0.1)Joins the game.
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
    
