from player import Player
from battalion import Battalion
import Presenter


class Gameplay:
    def __init__(self, firstPlayer, secondPlayer):
        self.player1 = firstPlayer
        self.player2 = secondPlayer
        self.current_player = firstPlayer
        self.opponent = secondPlayer

    @staticmethod
    def start_game():
        Presenter.present("Game started!")

    def check_victory(self):
        if not self.player1.army.units:
            Presenter.present(f"Player {self.player2.name} wins!")
            return True
        elif not self.player2.army.units:
            Presenter.present(f"Player {self.player1.name} wins!")
            return True
        return False

    def fight(self):
        while self.current_player.army.units and self.opponent.army.units:
            current_unit = self.current_player.army.units[0]
            opponent_unit = self.opponent.army.units[0]
            Presenter.present(f"ходит 1")
            Presenter.present(f"hp1 {current_unit.healthPoint} hp2 {opponent_unit.healthPoint}")
            opponent_unit.healthPoint -= current_unit.damage
            if opponent_unit.healthPoint <= 0:
                self.opponent.army.remove_unit(opponent_unit)
                continue
            Presenter.present(f"ходит 2")
            Presenter.present(f"hp1 {current_unit.healthPoint} hp2 {opponent_unit.healthPoint}")
            current_unit.healthPoint -= opponent_unit.damage
            if current_unit.healthPoint <= 0:
                self.current_player.army.remove_unit(current_unit)

    def play_game(self):
        self.start_game()
        while not self.check_victory():
            self.fight()


player1 = Player('p1', 'Human')
player2 = Player('p2', 'Elf')

Battalion.create_battalion(Battalion(), player1, [('LightAssault', 2), ('HeavyAssault', 1)])
Battalion.create_battalion(Battalion(), player2, [('LightAssault', 2), ('HeavyAssault', 1)])

game = Gameplay(player1, player2)

game.play_game()
