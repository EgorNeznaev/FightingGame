from typing import List, Tuple
from ArmyFactory import *
from player import Player
import Presenter


class Battalion:
    def __choose_battalion(self, player: [Player], Factory: [ArmyFactory], battalions: List[Tuple[str, int]]):
        for battalion in battalions:
            group = []
            for _ in range(battalion[1]):
                if battalion[0] == 'LightAssault':
                    group.append(Factory.create_light_assault(Factory))
                elif battalion[0] == 'HeavyAssault':
                    group.append(Factory.create_heavy_assault(Factory))

            if self.__check_cost(player, group):
                self.__add_battalion(player, group)

    @staticmethod
    def __check_cost(player: [Player], battalion: List[Unit]):
        if player.money > sum(unit.cost for unit in battalion):
            return True
        else:
            Presenter.present("You don't have enough money.")
            return False

    @staticmethod
    def __add_battalion(player: [Player], battalion: List[Unit]):
        for unit in battalion:
            if player.money >= unit.cost:
                player.army.add_unit(unit)
                player.money -= unit.cost

    def create_battalion(self, player: [Player], battalions: List[Tuple[str, int]]):
        if player.race == 'Human':
            self.__choose_battalion(player, HumanFactory, battalions)
        elif player.race == 'Elf':
            self.__choose_battalion(player, ElfFactory, battalions)
