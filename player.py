from Unit import *

class Player:
    def __init__(self, name, money=12):
        self.name = name
        self.money = money
        self.army = []

    def recruit(self, unit):
        if isinstance(unit, Unit):
            if self.money >= unit.cost:
                self.money -= unit.cost
                self.army.append(unit)
                print(f"{unit.name} has been recruited. Cost: {unit.cost}. Remaining money: {self.money}")
            else:
                print("Not enough money to recruit this unit.")
        else:
            print("Invalid unit object. It must be an instance of the Unit class.")




player = Player('p1')


soldier1 = Lightassaulte()
soldier2 = Heavyassaulte()


player.recruit(soldier1)
player.recruit(soldier2)
player.recruit(soldier2)

