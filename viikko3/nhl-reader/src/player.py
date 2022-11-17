
class Player:
    def __init__(self, name, team, goals, assists,):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        return self.name + "   team   " + self.team + "   goals   " + str(self.goals) + "  assists  " + str(self.assists)
    
    def get_goals(self):
        return self.goals
    
    def get_team(self):
        return self.team

    def get_assists(self):
        return self.assists
