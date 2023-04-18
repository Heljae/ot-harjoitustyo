from string import ascii_letters


class Board:
    """This class keeps track of the board.
    Starts from the beginning position.
    """

    def __init__(self):
        self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        self.fakefen = "rnbqkbnr/pppppppp/11111111/11111111/PPPPPPPP/RNBQKBNR"
        self.pieces = {"R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔",
                       "P": "♙", "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟"}
        self.whites_turn = True

    def print_board(self):
        board = ""
        row = ""
        for symbol in self.fen:
            if symbol == "/":
                row += "\n"
                board += row
                row = ""
                continue
            if symbol not in ascii_letters:
                row += int(symbol)*"."
                continue
            row += self.pieces[symbol]
            if len(board) == 63 and len(row) == 8:
                board += row
                break
        return board

    def board_without_icons_and_dots(self):
        board = ""
        row = ""
        for symbol in self.fen:
            if symbol == "/":
                row += "\n"
                board += row
                row = ""
                continue
            if symbol not in ascii_letters:
                row += int(symbol)*"."
                continue
            row += symbol
            if len(board) == 63 and len(row) == 8:
                board += row
                break
        board = board.replace(".", "1")
        return board

    def new_position_in_list(self, old_square: str, new_square: str, position: list):
        board_dict = self.board_list_to_dict(position)

        new_fen = ""
        old_rank_index = "87654321".find(old_square[-1])
        old_file_index = "abcdefgh".find(old_square[-2])
        new_rank_index = "87654321".find(new_square[-1])
        new_file_index = "abcdefgh".find(new_square[-2])

        if old_square[0] not in self.pieces:
            return "Vääräää"
        new_row = ""
        old_row = board_dict[old_rank_index]
        for i in range(8):
            if old_file_index == i:
                new_row += "1"
                continue
            new_row += old_row[i]
        board_dict[old_rank_index] = new_row

        new_row = ""
        older_row = board_dict[new_rank_index]
        for i in range(8):
            if new_file_index == i:
                new_row += old_square[0]
                continue
            new_row += older_row[i]
        board_dict[new_rank_index] = new_row

        return self.board_dict_to_list(board_dict)

    def board_list_to_dict(self, board: list):
        """Return the board in a dictionary
        """

        new_board = {}
        rank_index = 0
        for row in board:
            new_board[rank_index] = row
            rank_index += 1
        return new_board

    def board_dict_to_list(self, board: dict):
        """Returns the board in a list.
        """

        list_board = []
        for row in board:
            list_board.append(row)
        return list_board

    def new_fen(self, old_square: str, new_square: str, position: list):
        """Method creates a new fen where the given piece is moved into the given square.
        Method gets the previous square of the piece, the new square, and the board as its arguments.
        The board is a list where each row is in an index.
        """

        # This is still very broken

        new_fen = ""
        old_rank_index = "87654321".find(old_square[-1])
        old_file_index = "abcdefgh".find(old_square[-2])
        new_rank_index = "87654321".find(new_square[-1])
        new_file_index = "abcdefgh".find(new_square[-2])

        for i in range(8):
            if i == old_rank_index and old_square[0] in self.pieces:
                piece_leaving_rank = ""
                for j in range(8):
                    if j == old_file_index:
                        piece_leaving_rank += "1"
                    else:
                        piece_leaving_rank += position[i][j]
                position[i] = piece_leaving_rank
            if i == new_rank_index and new_square[0] in self.pieces:
                piece_new_to_rank = ""
                for j in range(8):
                    if j == new_file_index:
                        piece_new_to_rank += new_square[0]
                    else:
                        piece_new_to_rank += position[i][j]
                position[i] = piece_new_to_rank
            empty = 0
            new_row = ""
            for j in range(8):
                if position[i][j] == "1":
                    empty += 1
                elif empty == 0:
                    new_row += position[i][j]
                elif position[i][j] != "1" and empty != 0:
                    new_row += str(empty)
                    new_row += position[i][j]
                    empty = 0
            if j == 7 and empty != 0:
                new_row += str(empty)
            empty = 0
            new_fen += new_row+"/"

        return new_fen

# jee = Board()
# # print(jee.print_board())
# # print(jee.board_without_icons_and_dots())
# aa = ['rnbqkbnr', 'pppppppp', '11111111', '11111111', '11111111', '11111111', 'PPPPPPPP', 'RNBQKBNR']
# # print(jee.board_list_to_dict(aa))
# print(jee.new_fen("Ng1", "Nf3", aa))
