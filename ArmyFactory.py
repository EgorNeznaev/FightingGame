from abc import ABC, abstractmethod
from Unit import HumanLightAssault, HumanHeavyAssault, ElfHeavyAssault, ElfLightAssault, Unit


class ArmyFactory(ABC):
    @abstractmethod
    def create_light_assault(self) -> Unit:
        pass

    @abstractmethod
    def create_heavy_assault(self) -> Unit:
        pass


class HumanFactory(ArmyFactory):
    def create_light_assault(self) -> Unit:
        return HumanLightAssault()

    def create_heavy_assault(self) -> Unit:
        return HumanHeavyAssault()


class ElfFactory(ArmyFactory):
    def create_light_assault(self) -> Unit:
        return ElfLightAssault()

    def create_heavy_assault(self) -> Unit:
        return ElfHeavyAssault()
