import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_prints_the_board_correctly(self):
        test_board = self.board.print_board()

        self.assertEqual(
            "♜♞♝♛♚♝♞♜\n♟♟♟♟♟♟♟♟\n........\n........\n........\n........\n♙♙♙♙♙♙♙♙\n♖♘♗♕♔♗♘♖", test_board)
