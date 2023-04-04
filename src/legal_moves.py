class LegalMoves:
    """This class is for checking the possible legal moves of a piece.
    """

    def __init__(self):
        self.files = "abcdefgh"
        self.ranks = "12345678"

    def knights_legal_moves(self, square):
        """Returns all of knight's legal moves in the given square.
        """ 

        if square[1] not in self.files or square[2] not in self.ranks or len(square) != 3:  # chechs if the square is legal
            return "Illegal square!"

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

        if square[1] not in self.files or square[2] not in self.ranks or len(square) != 3:
            return "Illegal square!"
        
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

    def bishops_legal_moves(self, square):
        """Returns all of bishop's legal moves.
        """



        pass

    def queens_legal_moves(self, square):
        """Returns all of queen's legal moves.
        The queen can move like both rook and bishop, so the possible moves is the sum of the two.
        """

        if square[1] not in self.files or square[2] not in self.ranks or len(square) != 3:
            return "Illegal square!"

        return self.bishops_legal_moves(square) +self.rooks_legal_moves(square)

    def kings_legal_moves(self, square):
        """Returns all of king's legal moves.
        """

        file_index = "abcdefgh".find(square[1])
        rank_index = "12345678".find(square[2])

        if square[1] not in self.files or square[2] not in self.ranks or len(square) != 3:
            return "Illegal square!"

        possible_squares = {-1:[-1, 0, 1],0:[-1, 1],1:[-1,0,1]}
        legal_moves = []

        for move in possible_squares:
            if file_index-move < 0 or file_index+move > 7:
                continue
            for item in possible_squares[move]:
                if int(square[2])+item < 0 or int(square[2])+item > 7:
                    continue
                legal_moves.append(square[0]+(self.files[file_index+move])+(self.ranks[rank_index+item]))
        return legal_moves

    def white_pawns_legal_moves(self, square):
        """Returns all of white pawn's legal moves.
        Dictionary's key is file and value rank.
        Pawns can move either one or two squares in the beginning.
        Doesn't include captures or promotions.
        """

        if square[0] not in self.files or square[1] not in self.ranks or len(square) != 2:
            return "Illegal square!"

        possible_moves = [square[0]+str(int(square[1])+1)]
        if square[1] == "2":
            possible_moves.append(square[0]+str(int(square[1])+2))
        return possible_moves
    
    def black_pawns_legal_moves(self, square):
        """Returns all of black pawn's legal moves.
        """

        if square[0] not in self.files or square[1] not in self.ranks or len(square) != 2:
            return "Illegal square!"

        possible_moves = [square[0]+str(int(square[1])-1)]
        if square[1] == "7":
            possible_moves.append(square[0]+str(int(square[1])-2))
        return possible_moves

    