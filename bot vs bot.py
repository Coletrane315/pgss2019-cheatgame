import data_bot
import cheat
from cheat import client
import time

c=cheat.client.Client("Game_Maker")
c.create_game()
data_bot.run_bot("data1.csv")
data_bot.run_bot("data2.csv")
time.sleep(10)
c.start_game()
