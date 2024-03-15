from abc import ABC, abstractmethod
from Army import Army
from Unit import HumanLightAssault, HumanHeavyAssault, ElfHeavyAssault, ElfLightAssault


class ArmyFactory(ABC):
    @abstractmethod
    def create_light_assault(self, size: int) -> Army:
        pass

    @abstractmethod
    def create_heavy_assault(self, size: int) -> Army:
        pass


class HumanFactory(ArmyFactory):
    def create_light_assault(self, size: int) -> Army:
        army = Army()
        for _ in range(size):
            army.add_unit(HumanLightAssault())
        return army

    def create_heavy_assault(self, size: int) -> Army:
        army = Army()
        for _ in range(size):
            army.add_unit(HumanHeavyAssault())
        return army


class ElfFactory(ArmyFactory):
    def create_light_assault(self, size: int) -> Army:
        army = Army()
        for _ in range(size):
            army.add_unit(ElfLightAssault())
        return army

    def create_heavy_assault(self, size: int) -> Army:
        army = Army()
        for _ in range(size):
            army.add_unit(ElfHeavyAssault())
        return army
