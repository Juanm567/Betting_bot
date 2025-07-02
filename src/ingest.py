#Here we are going to ingest the data raw
import time
import pandas as pd
from datetime import datetime
from nba_api.stats.static import teams,players
from nba_api.stats.endpoints import playergamelog

#Get the current NBA season to pass to game logs
def get_current_season():
    year = datetime.today().year
    month = datetime.today().month

    if (month >= 10): #season starts in october
        start = year
        end = start + 1
    else:
        start = year - 1
        end = start + 1

    return f"{start}-{str(end)[-2:]}" #Make end a string and uses the last 2 digits for its desired format

#Get the team ID of both teams, players in the team, win / loss of the current league
def teams_info():
    nba_teams = teams.get_teams() #returns a list of dictionaries each being a team

    #team_name_id = {} #dictionary to hold key:full team name and value: team ID
    
    #for i in nba_teams:

        #team_name_id[i['full_name']] = i['id']
    
    return nba_teams


def players_info():
    nba_players = players.get_players() #returns a list of dictionaries each being a player
    active_players = [p for p in nba_players if p['is_active']]
    return active_players

    #players_name_id = {} #dict to get key:name and value:ID for active players

    #players_off = {} #dict to get key:name and value:ID for off players

    #for i in nba_players:

        #if(i['is_active']):
            #players_name_id[i['full_name']] = i['id']

        #else:
            #players_off[i['full_name']] = i['id']

    #return players_name_id, players_off

def game_logs(whole_info):
    all_dfs = []
    nba_season = get_current_season()
    players = players_info()
    def whole_game_logs():
        current_player = 1
        for player in players : #iterate through the list of active players
            print(f"getting data for players: [{current_player}/{len(players)}]",end = '\r',flush = True)#end = '\r' to overwrite the line allowing it to print on the same line not many
        # flush = True to ensure it prints immediately
            player_id = player['id']#find id of active player
            player_name = player['full_name']#get its full name
            try:
                result = playergamelog.PlayerGameLog(player_id=player_id, season=nba_season)#query object for the game log -> info held internally,return list of dataframes
                dfs = result.get_data_frames()[0]#access said dataframe since their is only one dataframe in the list
                if not dfs.empty:#if the df has data
                    all_dfs.append(dfs)#add the df to the list of df's
                #print(f"Fetched game log for {player_name} (ID: {player_id})")
                #testes for errors by doing print(f"{dfs.head()}\n")
            except Exception as e: #catch any exception that may occur during the query in a e variable
                print(f"Error fetching game log for {player_name} (ID: {player_id}): {e}")
            time.sleep(1) #sleep for 1 second to avoid hitting the API rate limit or you get some https error
            current_player += 1

        complete_df = pd.concat(all_dfs,ignore_index=True) #concatenate all the dataframes into one big dataframe
        print(complete_df) #print the first 5 rows of the dataframe to see if it worked
    if whole_info == True:
        whole_game_logs()
game_logs(False)







    

             







