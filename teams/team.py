from . import mock_data # dot operator goes up one level in the hierarchy and signals to python in the same package import yatayatayata can eityher do . one ..2 levels or ...3 levels
class Team:
    def __init__(self, team_name):
        #python is petty so variables and parameters should be lowercase bruhhh 
        self.team_name = team_name
        self.players = []
        self.benchednoff = []
        self.team_list()

    def team_list(self):
        for x in mock_data.mock_players:# Go over for loops in python
            if(x["is_playing"] == "Yes" and x["team_name"] == self.team_name ):# always write self.instance_variable to access dont be a dummy
                # if no body for the if statement is present you may use the keyword "pass" to skip the if statement in the loop
                self.players.append(x["name"])
            elif(x["is_playing"] == "No" and x["team_name"] == self.team_name):

                self.benchednoff.append(x["name"])
                
              

                

                


        

