from Unit import *
from ArmyFactory import ArmyFactory
from typing import List

class Player:
    def __init__(self, name, money=12):
        self.name = name
        self.money = money
        self.army = None

    def recruit(self, unit):
        if isinstance(unit, Unit):
            if self.money >= unit.cost:
                self.money -= unit.cost
                self.army.add_unit(unit)
                print(f"{unit.name} has been recruited. Cost: {unit.cost}. Remaining money: {self.money}")
            else:
                print("Not enough money to recruit this unit.")
        else:
            print("Invalid unit object. It must be an instance of the Unit class.")

    def create_army_with_factory(self, factories: List[ArmyFactory], sizes: List[int]):
        if len(factories) == len(sizes):
            for factory, size in zip(factories, sizes):
                self.army = factory.create_army(size)
        else:
            print("Invalid factory object. It must be an instance of the ArmyFactory class.")





