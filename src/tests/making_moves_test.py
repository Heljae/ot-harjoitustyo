import unittest
from logiikka.board import Board
from logiikka.making_moves import MakingMoves


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.moves = MakingMoves(Board("e2", "g7"))

    def test_moving_white_knight(self):
        board = self.moves.make_move("Nf3")
        correct = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                   '11111111', '11111N11', 'PPPPPPPP', 'RNBQKB1R']
        self.assertEqual(correct, board)

    # def test_moving_black_knight(self):
    #     board = self.moves.make_move("d4")
    #     board = self.moves.make_move("Nf6")
    #     correct = ['rnbqkb1r', 'pppppppp', '11111n11', '11111111',
    #                '11111111', '111P1111', 'PPP1PPPP', 'RNBQKBNR']
    #     self.assertEqual(correct, board)

    def test_moving_white_rook(self):
        board = self.moves.make_move("Rh4")
        correct = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                   '1111111R', '11111111', 'PPPPPPPP', 'RNBQKBN1']
        self.assertEqual(correct, board)

    # def test_moving_black_rook(self):
    #     board = MakingMoves(Board("d2", "a7"))

    #     move = self.moves.make_move("Nf3")
    #     move = self.moves.make_move("Rh5")
    #     correct = ['rnbqkbn1', 'pppppppp', '11111111', '1111111r',
    #                '1111111R', '11111N11', 'PPPPPPPP', 'RNBQKB1R']
    #     self.assertEqual(correct, move)

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

    def test_moving_white_pawn(self):
        board = self.moves.make_move("f4")
        correct = "rnbqkbnr/pppppppp/8/8/5P2/8/PPPPP1PP/RNBQKBNR"
        self.assertEqual(correct, board)

    def test_moving_black_pawn(self):
        board = self.moves.make_move("d4")
        board = self.moves.make_move("d5")
        correct = "rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR"
        self.assertEqual(correct, board)
