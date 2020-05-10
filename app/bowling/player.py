from app.bowling.score_keeper import ScoreKeeper

class Player:

    def __init__(self, player_name):
        self.player_name = player_name
        self.score = ScoreKeeper()
