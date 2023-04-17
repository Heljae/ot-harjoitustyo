from legal_moves import LegalMoves
from board import Board

class MakingMoves:
    """This class is meant for making moves on the chessboard
    The class gets a Board-type object
    """

    def __init__(self, board: Board):
        self.board = board
        self.position = board.fen
        self.turn = board.whites_turn
        self.legal = LegalMoves()
        self.rank = "12345678"
        self.file = "abcdefgh"
        self.pieces = "RNBKQrnbkq"

    def make_move(self, move):
        """This method makes the move and changes the position in attribute into FEN format.
        """

        if move[0] == "R":
            return self.__moving_rook(move)
        if move[0] == "N":
            return self.__moving_knight(move)

    def __moving_rook(self, move):
        legal_squares = self.legal.rooks_legal_moves(move)

        # We need to chech whose turn it is
        if self.turn == False:     # Laudan luokan totuusarvo ei toistaseks muutu   
            move = move.lower()
        board = self.board.board_without_icons_and_dots()
        board = board.split("\n")
        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "R"+self.file[j]+self.rank[i]
                    if self.turn == True:
                        if old in legal_squares and move[0] == "R":
                            self.turn = False
                            new_fen = self.board.new_fen(old, move, board)
                            return new_fen
                    else:
                        if old in legal_squares and move[0] == "r":
                            self.turn = True
                            new_fen = self.board.new_fen(old, move, board)
                            return new_fen
        raise ValueError("Laiton siirto!")

    def __moving_knight(self, move):
        pass

    def __moving_bishop(self, move):
        pass

    def __moving_queen(self, move):
        pass

    def __moving_king(self, move):
        pass

    def __moving_white_pawn(self, move):
        pass

    def __moving_black_pawn(self, move):
        pass


jee = MakingMoves(Board())
print(jee.make_move("Rh3"))
# jee.make_move("Ra8")