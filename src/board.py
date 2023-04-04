from string import ascii_letters

class Board:
    """This class keeps track of the board.
    Starts from the beginning position.
    """

    def __init__(self):
        self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        self.pieces = {"R":"♖","N":"♘","B":"♗","Q":"♕","K":"♔","P":"♙","r":"♜","n":"♞","b":"♝","q":"♛","k":"♚","p":"♟"}

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

