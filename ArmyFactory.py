from abc import ABC, abstractmethod
from Unit import Lightassaulte, Heavyassaulte

class ArmyFactory(ABC):
    @abstractmethod
    def create_army(self):
        pass

class PresetArmyFactory(ArmyFactory):
    def __init__(self, preset):
        self.preset = preset

    def create_army(self):
        if self.preset == 'light':
            return [Lightassaulte() for _ in range(5)]
        elif self.preset == 'heavy':
            return [Heavyassaulte() for _ in range(5)]
        else:
            raise ValueError(f"Unknown preset: {self.preset}")