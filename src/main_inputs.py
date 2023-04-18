from board import Board
from making_moves import MakingMoves


class Imputs:
    def main(self, number: int):
        if number == 1:
            return self.instructions()
        if number == 2:
            return self.num2()

    def instructions(self):
        print("1 - Printtaa ohjeet")
        print("2 - Tekee siirron")
        print("3 - Printtaa laudan")
        print("0 - Lopettaa ohjelman")

    def num2():
        pass
