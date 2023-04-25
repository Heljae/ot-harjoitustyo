from legal_moves import LegalMoves
from board import Board


class MakingMoves:
    """This class is meant for making moves on the chessboard
    The class gets a Board-type object
    """

    def __init__(self, board: Board):
        self.board = board
        self.position = board.fen
        self.turn = True
        self.legal = LegalMoves()
        self.rank = "87654321"
        self.file = "abcdefgh"
        self.pieces = "RNBKQrnbkq"

    def make_move(self, move):
        """This method makes the move and changes the position in attribute into FEN format.
        """

        if move[0] == "R":
            return self.__moving_rook(move)
        if move[0] == "N":
            return self.__moving_knight(move)
        if move[0] == "B":
            return self.__moving_bishop(move)
        if move[0] == "Q":
            return self.__moving_queen(move)
        if move[0] == "K":
            return self.__moving_king(move)
        if self.turn:
            return self.__moving_white_pawn(move)
        if not self.turn:
            return self.__moving_black_pawn(move)
        raise ValueError("Laiton siirto!")

        # if move[0] in moves:
        #     print(moves[move[0]])
        #     return moves[move[0]]

        # if move[0] in self.pieces:
        #     return moves[move[0]]
        # if move[0] in self.file:
        #     if self.turn:
        #         return self.__moving_white_pawn(move)
        #     if not self.turn:
        #         return self.__moving_black_pawn(move)
        # raise ValueError("Laiton siirto!")

    def __moving_rook(self, move):
        legal_squares = self.legal.rooks_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "R"+self.file[j]+self.rank[i]
        if self.turn:
            if old in legal_squares and move[0] == "R":
                self.turn = False
                position = self.board.new_position_in_list(
                    old, move, board)
                self.board.fen = self.board.new_fen(
                    old, move, board)
                return position
        else:
            move = move.lower()
            if old in legal_squares and move[0] == "r":
                self.turn = True
                position = self.board.new_position_in_list(
                    old, move, board)
                self.board.fen = self.board.new_fen(
                    old, move, board)
                return position
        raise ValueError("Laiton siirto!")

    def __moving_knight(self, move):
        legal_squares = self.legal.knights_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")

        if not self.turn:
            move = move.lower()

        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "N"+self.file[j]+self.rank[i]
                    if old in legal_squares:
                        break
        if self.turn:
            if old in legal_squares and move[0] == "N":
                self.turn = False
                position = self.board.new_position_in_list(
                    old, move, board)
                self.position = self.board.new_fen(
                    old, move, board)
                return position
        else:
            if old in legal_squares and move[0] == "n":
                self.turn = True
                position = self.board.new_position_in_list(
                    old, move, board)
                self.position = self.board.new_fen(
                    old, move, board)
                return position
        raise ValueError("Laiton siirto!")

    def __moving_bishop(self, move):
        legal_squares = self.legal.bishops_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "B"+self.file[j]+self.rank[i]
        if self.turn:
            if old in legal_squares and move[0] == "B":
                self.turn = False
                position = self.board.new_position_in_list(
                    old, move, board)
                self.position = self.board.new_fen(
                    old, move, board)
                return position
        else:
            move = move.lower()
            if old in legal_squares and move[0] == "b":
                self.turn = True
                position = self.board.new_position_in_list(
                    old, move, board)
                self.position = self.board.new_fen(
                    old, move, board)
                return position
        raise ValueError("Laiton siirto!")

    def __moving_queen(self, move):
        legal_squares = self.legal.queens_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "Q"+self.file[j]+self.rank[i]
        if self.turn:
            if old in legal_squares and move[0] == "Q":
                self.turn = False
                position = self.board.new_position_in_list(
                    old, move, board)
                self.position = self.board.new_fen(
                    old, move, board)
                return position
        else:
            move = move.lower()
            if old in legal_squares and move[0] == "q":
                self.turn = True
                position = self.board.new_position_in_list(
                    old, move, board)
                self.position = self.board.new_fen(
                    old, move, board)
                return position
        raise ValueError("Laiton siirto!")

    def __moving_king(self, move):
        legal_squares = self.legal.kings_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "K"+self.file[j]+self.rank[i]
        if self.turn:
            if old in legal_squares and move[0] == "K":
                self.turn = False
                position = self.board.new_position_in_list(
                    old, move, board)
                self.position = self.board.new_fen(
                    old, move, board)
                return position
        else:
            move = move.lower()
            if old in legal_squares and move[0] == "k":
                self.turn = True
                position = self.board.new_position_in_list(
                    old, move, board)
                self.position = self.board.new_fen(
                    old, move, board)
                return position
        raise ValueError("Laiton siirto!")

    def __moving_white_pawn(self, move):  # luokka edelleen rikki
        legal_squares = self.legal.white_pawns_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("\n")
        rank_index = "87654321".find(move[1])
        file_index = "abcdefgh".find(move[0])
        print(rank_index, file_index)
        for i in range(8):
            for j in range(8):
                if i == rank_index and j == file_index:
                    print(legal_squares)
                    old = self.file[j]+self.rank[i]
        if old in legal_squares:
            self.turn = False
            new_fen = self.board.new_fen(old, move, board)
            return new_fen
        raise ValueError("Laiton siirto!")

    def __moving_black_pawn(self, move):  # luokka rikki
        legal_squares = self.legal.black_pawns_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("\n")
        for i in range(8):
            for j in range(8):
                if i == move[0] and j == move[1]:
                    old = self.file[j]+self.rank[i]
        if old in legal_squares and move[0] == "p":
            self.turn = True
            new_fen = self.board.new_fen(old, move, board)
            return new_fen
        raise ValueError("Laiton siirto!")


# jee = MakingMoves(Board("e2", "g7"))
# print(jee.make_move("Nf3"))
# jee.make_move("Ra8")
