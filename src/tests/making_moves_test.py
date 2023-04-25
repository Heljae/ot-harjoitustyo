import unittest
from board import Board
from making_moves import MakingMoves


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.moves = MakingMoves(Board("e2", "g7"))

    def test_moving_white_knight(self):
        board = self.moves.make_move("Nf3")
        correct = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                   '11111111', '11111N11', 'PPPPPPPP', 'RNBQKB1R']
        self.assertEqual(correct, board)

    def test_moving_white_rook(self):
        board = self.moves.make_move("Rh4")
        correct = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                   '1111111R', '11111111', 'PPPPPPPP', 'RNBQKBN1']
        self.assertEqual(correct, board)

    def test_moving_white_bishop(self):
        board = self.moves.make_move("Be3")
        correct = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                   '11111111', '1111B111', 'PPPPPPPP', 'RN1QKBNR']
        self.assertEqual(correct, board)

    def test_moving_white_queen(self):
        board = self.moves.make_move("Qd5")
        correct = ['rnbqkbnr', 'pppppppp', '11111111', '111Q1111',
                   '11111111', '11111111', 'PPPPPPPP', 'RNB1KBNR']
        self.assertEqual(correct, board)

    def test_moving_white_king(self):
        board = self.moves.make_move("Kf1")
        correct = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                   '11111111', '11111111', 'PPPPPPPP', 'RNBQ1KNR']
        self.assertEqual(correct, board)

    # ahaa sotilas palauttaa tän eri muodossa lol
    def test_moving_white_pawn(self):
        board = self.moves.make_move("f4")
        correct = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                   '11111P11', '11111111', 'PPPPP1PP', 'RNBQKBNR']
        self.assertEqual(correct, board)
