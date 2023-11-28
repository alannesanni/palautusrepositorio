POINTS_0 = "Love"
POINTS_1 = "Fifteen"
POINTS_2 = "Thirty"
POINTS_3 = "Forty"

class TennisGame:
    def __init__(self, player1_name:str, player2_name:str):
        self.player1 = player1_name
        self.player2 = player2_name
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.score1 += 1
        if player_name == self.player2:
            self.score2 += 1

    def get_score(self):
        if self.is_tie():
            return self.tie_score()
        elif self.is_win():
            return self.win_score()
        return self.score()
    

    def is_tie(self):
        if self.score1 == self.score2:
            return True
        else:
            return False
        
    def tie_score(self):
        score=""
        if self.score1 == 0:
            score += POINTS_0
        elif self.score1 == 1:
            score += POINTS_1
        elif self.score1 == 2:
            score = score + POINTS_2
        else:
            return "Deuce"
        score += "-All"
        return score

    def score(self):
        score=""
        if self.score1 == 0:
            score += POINTS_0
        elif self.score1 == 1:
            score += POINTS_1
        elif self.score1 == 2:
            score = score + POINTS_2
        elif self.score1 == 3:
            score = score + POINTS_3
        score += "-"
        if self.score2 == 0:
            score += POINTS_0
        elif self.score2 == 1:
            score += POINTS_1
        elif self.score2 == 2:
            score = score + POINTS_2
        elif self.score2 == 3:
            score = score + POINTS_3
        return score
    
    def is_win(self):
        if self.score1 >= 4 or self.score2 >= 4:
            return True
        else:
            return False
        
    def win_score(self):
        minus_result = self.score1 - self.score2
        if minus_result == 1:
            score = f"Advantage {self.player1}"
        elif minus_result == -1:
            score = f"Advantage {self.player2}"
        elif minus_result >= 2:
            score = f"Win for {self.player1}"
        else:
            score = f"Win for {self.player2}"
        return score

