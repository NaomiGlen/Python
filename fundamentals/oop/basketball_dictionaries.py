class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']

    @classmethod
    def add_players(cls,data):
        player_objects = []
        for dictionary in data:
            player_objects.append(cls(dictionary))
        return player_objects

    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, Pos: {self.position}, Team: {self.team}"
        return display

    @classmethod
    def get_team(cls,team_list):
        team_objects = []
        for team in team_list:
            team_objects.append(cls(team))
        return team_objects

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
print(player_jason)
print(player_kevin)
print(player_kyrie)