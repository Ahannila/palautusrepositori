class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1


    def player_scores_under_4(self):
        return self.player1_score < 4 and self.player2_score < 4


    def score_situation_even_or_under_4(self):
        points_in_list = ["Love", "Fifteen", "Thirty", "Forty"]
        if self.player1_score >= 4 == self.player2_score >= 4:
            return 'Deuce'
        if self.player1_score == self.player2_score:
            s = points_in_list[self.player1_score]
            #print('tääl ollaa')
            return s+"-All"
        else:
            s = points_in_list[self.player1_score]
            #print('nyt ollaa tääl')
            return s +"-"+ points_in_list[self.player2_score]

    def score_advantage(self, player_name):
        if(abs(self.player1_score - self.player2_score))==1:
               score = "Advantage " + player_name
        else:
            score = "Win for " + player_name

        return score

    def game_is_even(self):
        return self.player1_score == self.player2_score

    def player1_leading(self):
        return self.player1_score > self.player2_score
    
    def player2_leading(self):
        return self.player2_score > self.player1_score
        
    def get_score(self):
        if self.game_is_even():
            score = self.score_situation_even_or_under_4()
            return score
        elif self.player_scores_under_4():
            #print('2')
            score = self.score_situation_even_or_under_4()
            return score
        elif self.player1_leading():
            score = self.score_advantage(self.player1_name)
            return score
        else: 
            score = self.score_advantage(self.player2_name)
            return score