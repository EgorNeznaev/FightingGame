from player import Player
from Unit import Unit, Lightassaulte, Heavyassaulte

class Gameplay:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.opponent = player2


    def start_game(self):
        print("Game started!")


    def check_victory(self):
        if not self.player1.army:
            print(f"Player {self.player2.name} wins!")
            return True
        elif not self.player2.army:
            print(f"Player {self.player1.name} wins!")
            return True
        return False

    def fight(self):
        while self.current_player.army and self.opponent.army:
            current_unit = self.current_player.army[0]
            opponent_unit = self.opponent.army[0]
            print(f"ходит 1")
            print(f"hp1 {current_unit.healthPoint} hp2 {opponent_unit.healthPoint}")
            opponent_unit.healthPoint -= current_unit.damage
            if opponent_unit.healthPoint <= 0:
                self.opponent.army.pop(0)
                continue
            print(f"ходит 2")
            print(f"hp1 {current_unit.healthPoint} hp2 {opponent_unit.healthPoint}")
            current_unit.healthPoint -= opponent_unit.damage
            if current_unit.healthPoint <= 0:
                self.current_player.army.pop(0)

    def play_game(self):
        self.start_game()
        while not self.check_victory():
            self.fight()


player1 = Player('p1')
player2 = Player('p2')


player1.recruit(Lightassaulte())
player1.recruit(Heavyassaulte())
player2.recruit(Heavyassaulte())
player2.recruit(Lightassaulte())

game = Gameplay(player1, player2)

game.play_game()