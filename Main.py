#Main program to run simulations based ond 
import pandas as pd
from teams.team import Team
from teams.player import Player
nba_players = {}
nba_players = players.get_players()
print(nba_players)
#How to get the player_id of a player in the api
#lebron = [player for player in nba_players if player['full_name'] == 'LeBron James'][0]
#print(f"LeBron James' player ID: {lebron['id']}")
dic = {}
for i in nba_players:
  dic[i['first_name']] = i['id']



for i,n in dic.items():
  print(f"{i}:{n}")








#player_names = []
#id = []
#for i in nba_players:
   #df = pd.DataFrame({'Player-Name':[i['full_name']],
                   #'Player_id': [i['id']]})
#print(df)
    

