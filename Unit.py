from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, healthPoint, damage, cost, name):
        self.healthPoint = healthPoint
        self.damage = damage
        self.cost = cost
        self.name = name

    @abstractmethod
    def attack(self, unit):
        pass


class HumanLightAssault(Unit):
    def __init__(self, healthPoint=25, damage=5, cost=3, name='LightAssault'):
        super().__init__(healthPoint, damage, cost, name)

    def attack(self, unit):
        damage_dealt = self.damage
        unit.healthPoint -= damage_dealt
        return damage_dealt


class HumanHeavyAssault(Unit):
    def __init__(self, healthPoint=40, damage=8, cost=4, name='HeavyAssault'):
        super().__init__(healthPoint, damage, cost, name)

    def attack(self, unit):
        damage_dealt = self.damage
        unit.healthPoint -= damage_dealt
        return damage_dealt


class ElfLightAssault(Unit):
    def __init__(self, healthPoint=18, damage=10, cost=3, name='LightAssault'):
        super().__init__(healthPoint, damage, cost, name)

    def attack(self, unit):
        damage_dealt = self.damage
        unit.healthPoint -= damage_dealt
        return damage_dealt


class ElfHeavyAssault(Unit):
    def __init__(self, healthPoint=25, damage=14, cost=5, name='HeavyAssault'):
        super().__init__(healthPoint, damage, cost, name)

    def attack(self, unit):
        damage_dealt = self.damage
        unit.healthPoint -= damage_dealt
        return damage_dealt
