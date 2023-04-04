class LegalMoves:
    """This class is for checking the possible legal moves of a piece.
    """

    def __init__(self):
        self.files = "abcdefgh"  # ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.ranks = "12345678" # [1, 2, 3, 4, 5, 6, 7, 8]

    def knights_legal_moves(self, square):
        """Returns all of knight's legal moves in the given square.
        """ 

        rank = int(square[2])
        file = square[1]
        file_index = "abcdefgh".find(square[1])
        rank_index = "12345678".find(square[2])

        """The following dictionary represents all of knight's possibe moves.
        The key is how many files the knight moves.
        The value is a list of how many ranks the knight can move.
        """
        possible_moves = {-2:[1, -1], -1:[2, -2], 1:[2, -2], 2:[1, -1]}
        moves = []
        for next_file in possible_moves:
            for item in possible_moves[next_file]:
                """We need to calculate if the knight goes over the board.
                """
                if rank_index+1+item > 8 or rank_index+1+item < 0:
                    continue
                if file_index+1+int(next_file) > 8 or file_index+1+int(next_file) < 1:
                    continue
                if rank_index + int(item) < 0:
                    continue
                moves.append(f"{square[0]}{self.files[file_index+int(next_file)]}{self.ranks[rank_index+int(item)]}")
        return moves
    
    def rooks_legal_moves(self, square):
        """Returns all of rook's legal moves.
        """
        
        rank = int(square[2])
        file = square[1]
        file_index = "abcdefgh".find(square[1])
        rank_index = "12345678".find(square[2])
        moves = []
        for letter in self.files:
            moves.append(square[0] + letter + str(rank))
        moves.remove(square)
        for number in self.ranks:
            moves.append(square[0] + str(file) + str(number))
        moves.remove(square)
        return moves

    def bishops_legal_moves():
        """Returns all of bishop's legal moves.
        """
        pass

    def queens_legal_moves():
        """Returns all of queen's legal moves.
        """
        pass

    def kings_legal_moves():
        """Returns all of king's legal moves.
        """
        pass

    def pawns_legal_moves():
        """Returns all of pawn's legal moves.
        """
        pass
    
if __name__=="__main__":
    jee = LegalMoves()
    print(jee.rooks_legal_moves("Rh8"))