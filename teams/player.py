from . import mock_data
class Player:
    def __init__(self,name):
        self.name = name
        for i in mock_data.mock_players:
            self.injured = i["injured"]
            self.is_playing = i["is_playing"]
            self.points_in_current_season = i["points_in_current_season"]
            self.average_points_per_season = i["average_points_per_season"]
        self.get_specifics()

    def get_specifics (self):
        return{
            'Name':self.name,
            'Injured':self.injured,
            'Is the player playing':self.is_playing,
            'points currently':self.points_in_current_season,
            'Average points in previous seasons':self.average_points_per_season,
        }

    #def player_power(self):


     