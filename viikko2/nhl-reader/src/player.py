import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists


    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.points}"

class PlayerReader:
    def __init__(self, url):
        self.url=url

    def get_players(self):
        response = requests.get(self.url).json()
        players=[]
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players

    
class PlayerStats:
    def __init__(self, players):
        self.players=players.get_players()
    
    def top_scorers_by_nationality(self, national):
        top_scores=[]
        for player in self.players:
            if player.nationality==national:
                top_scores.append(player)
        top_scores.sort(key=lambda p: p.points, reverse=True)
        return top_scores
            
