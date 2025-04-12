# Starters and Bench
player_list1_starters = [5, 5, 5, 5, 5]
player_list1_bench = [5, 5, 5, 5, 5]

player_list2_starters = [5, 5, 5, 5,5]
player_list2_bench = [5,5,5, 5,5]

# Total power (starters + bench)
team1_total = sum(player_list1_starters) + sum(player_list1_bench)
team2_total = sum(player_list2_starters) + sum(player_list2_bench)

# Difference in power
power_diff = abs(team1_total - team2_total)

# Decision logic
if power_diff <= 4:
    print("Very close game. Displaying win chances:")
    team1_win = team1_total / (team1_total + team2_total)
    team2_win = team2_total / (team1_total + team2_total)
    print(f"Team 1 win chance: {team1_win * 100:.2f}%")
    print(f"Team 2 win chance: {team2_win * 100:.2f}%")
elif team1_total > team2_total:
    print("Team 1 is favored to win.")
else:
    print("Team 2 is favored to win.")


    



