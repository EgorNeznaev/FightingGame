from Unit import Unit


class Army:
    def __init__(self):
        self.units = []

    def add_unit(self, unit: Unit):
        self.units.append(unit)

    def remove_unit(self, unit: Unit):
        self.units.remove(unit)
