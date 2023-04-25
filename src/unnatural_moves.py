class AbnormalMoves:
    """This class is for making abnormal moves that do something.
    In this case abnormal moves are captures, checks and checkmates.
    """

    def checking_captures(self, move):
        """This method is for cheking if a move was a capture.
        """

        capture = move.find("x")

        if capture == -1:
            return
        
        if move[0] not in "RNBQK":
            piece = "p"
        
    def checkmate(self, fen):
        pass

    def check(self, fen):
        pass

    def checks_next_move(self, move):
        """If the move after the check wasn't made with a king,
        or the check wasn't blocked, the move was illegal.
        """
        pass