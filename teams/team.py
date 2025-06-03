from . import mock_data # dot operator goes up one level in the hierarchy and signals to python in the same package import yatayatayata can eityher do . one ..2 levels or ...3 levels
class Team:
    def __init__(self, team_id):
        #python is petty so variables and parameters should be lowercase bruhhh 
        self.team_id = team_id
        self.players = []
        self.team_list()

    def team_list(self):
        for x in mock_data.mock_players:
            if(x["is_playing"] == True and x["team_id"] == self.team_id ):# always write self.instance_variable to access dont be a dummy
                # if no body for the if statement is present you may use the keyword "pass" to skip the if statement in the loop
                self.players.append(x["name"])
                
              

                

                


        

