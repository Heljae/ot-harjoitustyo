from string import ascii_letters


class Board:
    """This class keeps track of the board.
    Starts from the beginning position.
    """

    def __init__(self, queen1, queen2):
        self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        self.unseen_fen = "rnbqkbnr/pppppppp/11111111/11111111/11111111/11111111/PPPPPPPP/RNBQKBNR"
        self.queen1 = queen1
        self.queen2 = queen2
        self.pieces = {"R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔",
                       "P": "♙", "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟"}

    def print_board(self):
        board = ""
        row = ""
        for symbol in self.fen:
            if symbol == "/":
                board += row+"\n"
                row = ""
                continue
            if symbol not in ascii_letters:
                row += int(symbol)*". "
                continue
            row += self.pieces[symbol]+" "
        board += row
        return board

    def board_setup(self):
        """This method sets up the board correctly for a game.
        """

        board = self.unseen_fen
        board = board.split("/")
        fen = ""
        file_index1 = "abcdefgh".find(self.queen1[-2])
        file_index2 = "abcdefgh".find(self.queen2[-2])
        row = ""

        # Next checks if the given queens are valid
        if self.queen1[1] != "2" or self.queen2[1] != "7":
            return False

        # Next sets up the nonvisible board
        for i in range(8):
            if i != 1 and i != 6:
                fen += board[i]
                if i != 7:
                    fen += "/"
                continue
            for j in range(8):
                if i == 1:
                    if j == file_index2:
                        row += "q"
                    else:
                        row += board[i][j]
                if i == 6:
                    if j == file_index1:
                        row += "Q"
                    else:
                        row += board[i][j]
            fen += row+"/"
            row = ""

        self.unseen_fen = fen
        return True

    # def making_unseen_board(self):
    #     board = ""
    #     row = ""
    #     for symbol in self.unseen_fen:
    #         if symbol == "/":
    #             board += row+"/"
    #             row = ""
    #             continue
    #         if symbol not in ascii_letters:
    #             row += "1"
    #             continue
    #         row += symbol
    #     board += row
    #     return board

    def board_without_icons_and_dots(self):
        board = ""
        row = ""
        for symbol in self.fen:
            if symbol == "/":
                board += row+"/"
                row = ""
                continue
            if symbol not in ascii_letters:
                row += int(symbol)*"1"
                continue
            row += symbol
        board += row
        return board

    def new_position_in_list(self, old_square: str, new_square: str, position: list):
        board_dict = self.board_list_to_dict(position)
        old_rank_index = "87654321".find(old_square[-1])
        old_file_index = "abcdefgh".find(old_square[-2])
        new_rank_index = "87654321".find(new_square[-1])
        new_file_index = "abcdefgh".find(new_square[-2])
        piece = new_square[0]

        if piece not in self.pieces:
            if old_rank_index-new_rank_index < 0:
                piece = "p"
            else:
                piece = "P"

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
                new_row += piece
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
        for i in range(8):
            list_board.append(board[i])
        return list_board

    def new_fen(self, old_square: str, new_square: str, position: list):
        """Method creates a new fen where the given piece is moved into the given square.
        Method gets the previous square of the piece, the new square, and the board as arguments.
        The board is a list where each row is in an index.
        """

        # self.unseen_fen = self.board_without_icons_and_dots()

        board = self.new_position_in_list(old_square, new_square, position)
        empty = 0
        new_fen = ""

        for i in range(8):
            new_row = ""
            for j in range(8):
                if board[i][j] == "1":
                    empty += 1
                    continue
                if empty == 0:
                    new_row += board[i][j]
                    continue
                new_row += str(empty)
                new_row += board[i][j]
                empty = 0
            if empty != 0:
                new_row += str(empty)
            empty = 0
            new_fen += new_row
            if i != 7:
                new_fen += "/"
        self.fen = new_fen
        return new_fen


# jee = Board("e2", "g7")
# print(jee.board_setup())
# print(jee.unseen_fen)
# print(jee.print_board())
# print(jee.board_without_icons_and_dots())
# print(jee.unseen_fen)
# aa = ['rnbqkbnr', 'pppppppp', '11111111', '11111111', '11111111', '11111111', 'PPPPPPPP', 'RNBQKBNR']
# aa1 = ['rnbqkbnr', 'pppppppp', '11111111', '11111111', '11111111', '11111N11', 'PPPPPPPP', 'RNBQKB1R']
# aa = ['rnbq1rk1', 'pppp1ppp', '1111pn11', '11111111', '1bPP1111', '11N1P111', 'PP111PPP', 'R1BQKBNR']
# print(jee.board_list_to_dict(aa))
# print(jee.new_fen("Ng1", "Nf3", aa))
# print(jee.board_list_to_dict(aa))
