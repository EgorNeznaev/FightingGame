from Army import Army


class Player:
    def __init__(self, name, race, money=12):
        self.name = name
        self.race = race
        self.money = money
        self.army = Army()
