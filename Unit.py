from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, healthpoint, damage, cost):
        self.healthPoint = healthpoint
        self.damage = damage
        self.cost = cost

    @abstractmethod
    def attack(self, unit):
        pass


class Lightassaulte(Unit):
    def __init__(self, healthpoint, damage, cost):
        super().__init__(healthpoint, damage, cost)

    def attack(self, unit):
        damagedealt = self.damage
        unit.healthPoint -= damagedealt
        return damagedealt