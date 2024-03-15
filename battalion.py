from typing import List, Tuple
from ArmyFactory import *
from player import Player
import Presenter


class Battalion:
    def __choose_battalion(self, player: [Player], Factory: [ArmyFactory], battalions: List[Tuple[str, int]]):
        for battalion in battalions:
            battalion_army = None
            if battalion[0] == 'LightAssault':
                battalion_army = Factory.create_light_assault(Factory, battalion[1])
            elif battalion[0] == 'HeavyAssault':
                battalion_army = Factory.create_heavy_assault(Factory, battalion[1])

            if self.__check_cost(player, battalion_army):
                self.__add_battalion(player, battalion_army)

    @staticmethod
    def __check_cost(player: [Player], battalion: [Army]):
        if player.money > sum(unit.cost for unit in battalion.units):
            return True
        else:
            Presenter.present("You don't have enough money.")
            return False

    @staticmethod
    def __add_battalion(player: [Player], battalion: [Army]):
        for unit in battalion.units:
            if player.money >= unit.cost:
                player.army.add_unit(unit)
                player.money -= unit.cost

    def create_battalion(self, player: [Player], battalions: List[Tuple[str, int]]):
        if player.race == 'Human':
            self.__choose_battalion(player, HumanFactory, battalions)
        elif player.race == 'Elf':
            self.__choose_battalion(player, ElfFactory, battalions)
