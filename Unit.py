from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, healthpoint, damage, cost, name):
        self.healthPoint = healthpoint
        self.damage = damage
        self.cost = cost
        self.name = name

    @abstractmethod
    def attack(self, unit):
        pass


class Lightassaulte(Unit):
    def __init__(self, healthpoint=20, damage=5, cost=2, name='Lightassaulte'):
        super().__init__(healthpoint, damage, cost, name)

    def attack(self, unit):
        damagedealt = self.damage
        unit.healthPoint -= damagedealt
        return damagedealt


class Heavyassaulte(Unit):
    def __init__(self, healthpoint=30, damage=7, cost=5, name='Heavyassaulte'):
        super().__init__(healthpoint, damage, cost, name)

    def attack(self, unit):
        damagedealt = self.damage
        unit.healthPoint -= damagedealt
        return damagedealt
