import cheat
from cheat import client
import time
import random

def run_bot():

    in_progress=False
    load_time=True
    name = input('input username')
    c=cheat.client.Client(name)

    games = c.list_games()
    print(games)
    game_id = input('input game id')

    join_game(c,game_id)

    message = c.wait_for_message()
    print(message)

    
    while True:
        #start playing the game here
        c.update_game()
        c.update_player_info()
        time.sleep(0.5)
        c.hand.sort(key=lambda x:x['Value'])

        state = c.get_current_turn()

        
        if load_time==True:
            time.sleep(1)
            load_time=False

        
        if int(state['Position']) == c.position:
            next_turn=state['Position']
            c.update_player_info()
            time.sleep(0.5)
            c.hand.sort(key=lambda x:x['Value'])
            print(c.hand)

            print('You are playing ')
            print((c.get_current_turn()['CardValue']))
            x = []
            hand = c.hand
            y = int(input("Which number are you playing? Enter -1 to stop choosing "))
            while y != -1 or len(x) == 0:
                check = False
                for cards in hand:
                    if cards['Value'] == y:
                        x.append(cards)
                        hand.remove(cards)
                        check = True
                if check == False:
                    print("Card not in hand")
                y = int(input("Which number are you playing? Enter -1 to stop choosing "))
                      
            c.play_cards(x)
            
            time.sleep(1)
            c.update_player_info()
            #print(c.hand)

            message = c.wait_for_message()
            print(message)
            if(message[0] == 'GAME_OVER'):
                print ("Game Over: Position: " + str(message['WinningPosition']) + " won!")
                return
            message = c.wait_for_message()
            print(message)
            if(message[0] == 'CALLED'):
                print("Somebody called bluff")
                if(message[1][1]['WasLie']):
                    print("It was a lie")
                else:
                    print("It was not a lie")
                message = c.wait_for_message()
                print(message)
                print("Turn Over")
            
        elif int(state['Position'])!= c.position:
            message = c.wait_for_message()
            turn = c.get_current_turn()
            print("Player " + str(turn['Position']) + " played ")
            print (turn['CardsDown'])
            print((turn['CardValue']))
            print("Your Hand: " + str(c.hand))
            x = input("Pass or Call?")
            while True:
                if x == "Pass":
                    c.play_pass()
                    break
                elif x == "Call":
                    c.play_call()
                    break
                else:
                    print("Invalid Input")
                    x = input("Pass or Call?")
            time.sleep(0.1)
            c.update_player_info()
            message = c.wait_for_message()
            print(message)
            if(message[0] == 'GAME_OVER'):
                print ("Game Over: Position: " + str(message['WinningPosition']) + " won!")
                return
            if(message[0] == 'CALLED'):
                print("Somebody called bluff")
                if(message[1][1]['WasLie']):
                    print("It was a lie")
                else:
                    print("It was not a lie")
                message = c.wait_for_message()
                print(message)
                print("Turn Over")

        time.sleep(0.1)

def join_game(client,game_id):
    c=client
    c.game_id=game_id
    c.join_game()
    c.update_game()
    c.update_player_info()

"""
Starts the game and initializes the variables within game_state.
"""
def get_number_val(self,card_val):
    if isinstance(card_val,list):
        card_val=card_val[1]
    if card_val=="Ace":
        return 1
    elif card_val=="Jack":
        return 11
    elif card_val=="Queen":
        return 12
    elif card_val=="King":
        return 13
    return int(card_val)
    


if __name__ == '__main__':
    run_bot()
    
