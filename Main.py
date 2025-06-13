import numpy as np
import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


nba_player = players.get_players()  #Get player id, player name, id, if they are playing
user_value = input("Get info for the following player: ")
for player in nba_player:
  if(player['full_name'] == user_value and player['is_active'] == True):
    print(f"Name: {player['full_name']}\nPlayer ID: {player['id']}\n\n")
    player_id = player['id']
    # Fetch career stats for a player by ID
  career = playercareerstats.PlayerCareerStats(player_id)
  career_data = career.get_data_frames()[0]
    # Show the first few rows of the data
  print(career_data)  






