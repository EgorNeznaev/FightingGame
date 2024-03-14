from abc import ABC, abstractmethod
from Unit import Lightassaulte, Heavyassaulte
from Army import Army

class ArmyFactory(ABC):
    @abstractmethod
    def create_army(self, size: int) -> Army:
        pass

class LightArmyFactory(ArmyFactory):
    def create_army(self, size: int) -> Army:
        army = Army()
        for _ in range(size):
            army.add_unit(Lightassaulte())
        return army

class HeavyArmyFactory(ArmyFactory):
    def create_army(self, size: int) -> Army:
        army = Army()
        for _ in range(size):
            army.add_unit(Heavyassaulte())
        return army
