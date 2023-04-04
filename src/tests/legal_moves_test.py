import unittest
from legal_moves import LegalMoves

class TestLegalMoves(unittest.TestCase):
    def setUp(self):
        self.legal = LegalMoves()

    def test_knights_legal_squares(self):
        moves = self.legal.knights_legal_moves("Nh2")

        self.assertEqual(sorted(["Nf1", "Nf3", "Ng4"]), sorted(moves))

    def test_knights_legal_squares2(self):
        moves = self.legal.knights_legal_moves("Nd8")

        self.assertEqual(sorted(["Nb7", "Nc6", "Ne6", "Nf7"]), sorted(moves))

    def test_knights_legal_squares_illegal_input(self):
        moves = self.legal.knights_legal_moves("N2e")

        self.assertEqual("Illegal square!", moves)