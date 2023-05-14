import unittest
from logiikka.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board("e2", "g7")

    def test_prints_the_board_correctly(self):
        test_board = self.board.print_board()
        self.assertEqual(
            "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n. . . . . . . . \n. . . . . . . . \n. . . . . . . . \n. . . . . . . . \n♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ ", test_board)

    def test_board_setup_changes_the_unseen_fen(self):
        self.board.board_setup()
        self.assertEqual(
            "rnbqkbnr/ppppppqp/11111111/11111111/11111111/11111111/PPPPQPPP/RNBQKBNR", self.board.unseen_fen)

    def test_board_setup_correct_output(self):
        output = self.board.board_setup()
        self.assertEqual(True, output)

    def test_board_setup_correct_output_when_invalid_queens(self):
        board = Board("e7", "g2")
        output = board.board_setup()
        self.assertEqual(False, output)

    def test_board_without_icons_and_dots(self):
        board = self.board.board_without_icons_and_dots()
        self.assertEqual(
            "rnbqkbnr/pppppppp/11111111/11111111/11111111/11111111/PPPPPPPP/RNBQKBNR", board)

    def test_new_position_in_list_rook(self):
        board = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                 '11111111', '11111111', 'PPPPPPPP', 'RNBQKBNR']
        position = self.board.new_position_in_list("Rh1", "Rh3", board)
        self.assertEqual(['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                         '11111111', '1111111R', 'PPPPPPPP', 'RNBQKBN1'], position)

    def test_new_position_in_list_black_knight(self):
        board = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                 '11111111', '11111111', 'PPPPPPPP', 'RNBQKBNR']
        position = self.board.new_position_in_list("Ng8", "nf6", board)
        self.assertEqual(['rnbqkb1r', 'pppppppp', '11111n11', '11111111',
                         '11111111', '11111111', 'PPPPPPPP', 'RNBQKBNR'], position)

    def test_board_list_to_dict(self):
        board = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                 '11111111', '11111111', 'PPPPPPPP', 'RNBQKBNR']
        correct_dict = {0: 'rnbqkbnr', 1: 'pppppppp', 2: '11111111', 3: '11111111',
                        4: '11111111', 5: '11111111', 6: 'PPPPPPPP', 7: 'RNBQKBNR'}
        dict_board = self.board.board_list_to_dict(board)
        self.assertEqual(correct_dict, dict_board)

    def test_board_dict_to_list(self):
        correct_list = ['rnbqkbnr', 'pppppppp', '11111111',
                        '11111111', '11111111', '11111111', 'PPPPPPPP', 'RNBQKBNR']
        board_dict = {0: 'rnbqkbnr', 1: 'pppppppp', 2: '11111111', 3: '11111111',
                      4: '11111111', 5: '11111111', 6: 'PPPPPPPP', 7: 'RNBQKBNR'}
        board = self.board.board_dict_to_list(board_dict)
        self.assertEqual(correct_list, board)

    def test_new_fen(self):
        board = ['rnbqkbnr', 'pppppppp', '11111111', '11111111',
                 '11111111', '11111111', 'PPPPPPPP', 'RNBQKBNR']
        fen = self.board.new_fen("d2", "d4", board)
        correct_fen = "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR"
        self.assertEqual(correct_fen, fen)
