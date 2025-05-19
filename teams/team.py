import mock_data
class Team:
    def __init__(self, team_id):
        self.team_id = team_id
        self.players = []
        for x in mock_data.mock_players:
            if x["is_playing" and x"Team_id" == team_id]:
        #Need to append to list and instantiate player class

