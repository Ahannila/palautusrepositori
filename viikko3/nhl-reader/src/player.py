
class Player:
    def __init__(self, name, team, goals, assists,):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        sum = self.goals+self.assists
        return f"{self.name:25}" + f"{self.team:6}" + f"{str(self.goals):2}" + "  +  " + f"{str(self.assists):2}" + " = " + str(sum)
    
    def get_goals(self):
        return self.goals
    
    def get_team(self):
        return self.team

    def get_assists(self):
        return self.assists
