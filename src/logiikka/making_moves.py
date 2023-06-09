from logiikka.legal_moves import LegalMoves
from logiikka.board import Board


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

#         >>> command = 'Hello, World!'
# >>> match command:
# ...     case 'Hello, World!':
# ...         print('Hello to you too!')
# ...     case 'Goodbye, World!':
# ...         print('See you later')
# ...     case other:
# ...         print('No match found')
 
# Hello to you too!

        match move[0]:
            case "R":
                return self.__moving_rook(move)
            case "N":
                return self.__moving_knight(move)
            case "B":
                return self.__moving_bishop(move)
            case "Q":
                return self.__moving_queen(move)
            case "K":
                return self.__moving_king(move)
        if self.turn:
            return self.__moving_white_pawn(move)
        if not self.turn:
            return self.__moving_black_pawn(move)
        raise ValueError("Laiton siirto!")

    def __moving_rook(self, move):
        legal_squares = self.legal.rooks_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "R"+self.file[j]+self.rank[i]
        if old not in legal_squares:
            print("Laiton siirto, anna uusi siirto!")
            return

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
        if old not in legal_squares:
            print("Laiton siirto, anna uusi siirto!")
            return

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

    def __moving_bishop(self, move):
        legal_squares = self.legal.bishops_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "B"+self.file[j]+self.rank[i]
                    if old in legal_squares:
                        break
        if old not in legal_squares:
            print("Laiton siirto, anna uusi siirto!")
            return

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

    def __moving_queen(self, move):
        legal_squares = self.legal.queens_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "Q"+self.file[j]+self.rank[i]
                    if old in legal_squares:
                        break
        if old not in legal_squares:
            print("Laiton siirto, anna uusi siirto!")
            return

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

    def __moving_king(self, move):
        legal_squares = self.legal.kings_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        for i in range(8):
            for j in range(8):
                if board[i][j] == move[0]:
                    old = "K"+self.file[j]+self.rank[i]
                    if old in legal_squares:
                        break
        if old not in legal_squares:
            print("Laiton siirto, anna uusi siirto!")
            return
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

    def __moving_white_pawn(self, move):
        legal_squares = self.legal.white_pawns_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        rank_index = "87654321".find(move[-1])
        file_index = "abcdefgh".find(move[-2])

        if board[rank_index+1][file_index] == "P":
            old = self.file[file_index]+self.rank[rank_index+1]
        else:
            old = self.file[file_index]+self.rank[rank_index+2]

        if old not in legal_squares:
            print("Laiton siirto, anna uusi siirto!")
            return
        self.turn = False
        new_fen = self.board.new_fen(old, move, board)
        return new_fen

    def __moving_black_pawn(self, move):  # rikki
        legal_squares = self.legal.black_pawns_legal_moves(move)

        board = self.board.board_without_icons_and_dots()
        board = board.split("/")
        rank_index = "87654321".find(move[-1])
        file_index = "abcdefgh".find(move[-2])

        if board[rank_index-1][file_index] == "p":
            old = self.file[file_index]+self.rank[rank_index-1]
        else:
            old = self.file[file_index]+self.rank[rank_index-2]

        if old not in legal_squares:
            print("Laiton siirto, anna uusi siirto!")
            return
        self.turn = True
        new_fen = self.board.new_fen(old, move, board)
        return new_fen
