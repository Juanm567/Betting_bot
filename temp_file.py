from nba_api.stats.static import players,teams
nba_players = {}
nba_players = players.get_players()
print(nba_players)