#Main program to run simulations based ond 
from teams.team import Team
print("Commands:\n\n Player - \"player name\"\n Team - \"Team name\"\n Player-stats - \"Player name\"")
team = input("Team 1:")
team_2 = input("Team 2:")
TL = Team(team)
TL = Team(team_2)
print("Starters for " + team, ":", TL.players,"\nBenched / off for " + team,":",TL.benchednoff, "\n")
print("\n\nStarters for " + team_2, ":", TL.players,"\nBenched / off for " + team_2,":",TL.benchednoff, "\n")
 

#player_list1_starters = [100, 100, 100,100,100]
#player_list1_bench = [100,100,100,100,100]

#player_list2_starters = [100,100,100,100,100]
#player_list2_bench = [100,100,100,100,100]

# Total power (starters + bench)
#team1_total = sum(player_list1_starters) + sum(player_list1_bench)
#team2_total = sum(player_list2_starters) + sum(player_list2_bench)

# Difference in power
#power_diff = abs(team1_total - team2_total)

# Decision logic / will change
#if power_diff <= 4:
  #  print("Very close game. Displaying win chances:")
  #  team1_win = team1_total / (team1_total + team2_total)
  #  team2_win = team2_total / (team1_total + team2_total)
  # print(f"Team 1 win chance: {team1_win * 100:.2f}%")
  #  print(f"Team 2 win chance: {team2_win * 100:.2f}%")
#elif team1_total > team2_total: 
 #print("Team 1 is favored to win.")
#else:
 #   print("Team 2 is favored to win.")


    



