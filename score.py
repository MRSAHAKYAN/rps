class ScoreManager:
    def __init__(self, players):
        self.score_table = {player.get_name() : 0 for player in players }
        
    def get_score(self, name):
        return self.score_table[name]
    
    def add_score(self, name, value=1):
        self.score_table[name] += value