#Handle class calls and the instantiation of the discord bot therefore this is the main entry point which will be what runs my entire data pipeline
from src import features
import sys
#set up variable for the list of player names
player_names = []
instructions = {
    'Player_games:' : " # of games to lookup, player name",
    'Team_games:': " # of games to lookup, Team name",
    'player_stats:': " player name, yes or no if you want a graph of points in recent games",
    'Team_vs_Team:' : " Team1 name, Team2 name",
    'Player_vs_Player:' : " Player1 name, Player2 name"
    }
command_actions = {
   'player_games':features.player_games,#use dynamic arguments to decide argsfor functions in runtime
   'team_games':features.team_games,
   'player_stats':features.player_stats,
   'team_vs_team':features.tvt,
   'player_vs_player':features.pvp,
   'get_all_players':features.p_all
}
print("\n\nWelcome to the easy NBA info lookup program so far we only support player and team data but machine learning predictions are in the works\n\n")

print("What would you like to lookup?\n")
print("Type 'done' to exit")
for key , value in (instructions.items()):
    print(f"{key}{instructions[key]}\n")
while(True):
 user_in= input("-->")
 if user_in.lower() == 'done': sys.exit(0)
 slicing = user_in.strip().split()
 command = slicing[0]
 args = slicing[1:]
 print(args)
 #might use tkinter to make a GUI for this later or something to make it easier to pass arguments to functions then handling data and we should be good for v1
 








