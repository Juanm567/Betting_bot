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
    nba_teams = teams.get_teams() #returns a list of dictionaries each beiong a team

    #team_name_id = {} #dictionary to hold key:full team name and value: team ID
    
    #for i in nba_teams:

        #team_name_id[i['full_name']] = i['id']
    
    return nba_teams


def players_info():
    nba_players = players.get_players() #returns a list of dictionaries each being a player

    #players_name_id = {} #dict to get key:name and value:ID for active players

    #players_off = {} #dict to get key:name and value:ID for off players

    #for i in nba_players:

        #if(i['is_active']):
            #players_name_id[i['full_name']] = i['id']

        #else:
            #players_off[i['full_name']] = i['id']

    #return players_name_id, players_off
    return nba_players

def game_logs():
    id_list = [] #List to have player ids to use in game logs lookup
    all_dfs = [] # store all the df of player game logs in a list
    nba_players = players_info() #must call the players_info() method to get the raw player_data
    nba_season = get_current_season()

    for i in nba_players:

        id_list.append(i['id'])

    for j in id_list:

        try: #Handle issue if an error occurs when making the API call e.g (missing ID, wrong season format, etc)
            df = playergamelog.playerGamelog(player_id = j, season = nba_season).get_data_frames()[0] #access player logs
            #[0] referes to you getting the df in the list that is returned by .get_data_frames 
            all_dfs.append(df)
        except:
            print(f"Error extracting data can not get data for player with ID {j}")

        time.sleep(0.6)# deals with API rate limits

    complete_df = pd.concat(all_dfs,ignore_index=True) #concatenate the df's in all_dfs into a single bigger dataframe with a new index ignoring those from og df

    return complete_df





    

             







