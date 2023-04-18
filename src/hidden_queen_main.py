from board import Board
from making_moves import MakingMoves

"""Works first like regular chess
"""

print("Tervetuloa pelaamaan shakin varianttia nimeltä Piilodaami!")
print()
print("Ohjelma vaatii englanninkielisen shakkinotaation tuntemisen.")
print("1 - Printtaa ohjeet")
print("2 - Tekee siirron")  # Works only when you move the rook once :')
print("3 - Printtaa laudan")
print("0 - Lopettaa ohjelman")
print()

position = Board()
real_position = MakingMoves(position)

while True:
    instruction = int(input("Anna ohje: "))
    if instruction == 0:
        print("Kiitos pelaamisesta!")
        break
    elif instruction == 1:
        print("1 - Printtaa ohjeet")
        print("2 - Tekee siirron")
        print("3 - Printtaa laudan")
        print("0 - Lopettaa ohjelman")
    elif instruction == 3:
        print()
        print(position.print_board())
    elif instruction == 2:
        move = input(
            "Anna siirto (kokeile Rh3 ja printtaa sen jälkeen lauta):")
        moving = real_position.make_move(move)
        print()


# from board import Board
# from legal_moves import LegalMoves

# jee = Board()
# print(jee.print_board())
# jee2 = LegalMoves()
# print(jee2.black_pawns_legal_moves("e4"))
# print(jee2.white_pawns_legal_moves("f2"))
# print(jee2.knights_legal_moves("Nh1"))
# print(jee2.rooks_legal_moves("Rh9"))
# print(jee2.kings_legal_moves("Ke4"))
# print(jee2.bishops_legal_moves("Be4"))
# print(jee2.queens_legal_moves("Qc6"))
