from board import Board
from making_moves import MakingMoves
from unnatural_moves import AbnormalMoves

print("Tervetuloa pelaamaan shakin varianttia nimeltä Piilodaami!")
print()
print("Pelin alussa molemmat pelaajat valitsevat yhden sotilaistaan, joka")
print("saakin liikkua kuningattaren tavoin. Kuningatar näyttää kuitenkin")
print("edelleen sotilaalta. Muuten peli noudattaa normaaleja shakin sääntöjä.")
print("Enter lopettaa pelin.")
print("Ohjelma vaatii englanninkielisen shakkinotaation tuntemisen.")
print()

print("Valitse yksi sotilaistasi, jonka haluat olevan kunignatar.")
print("Kirjoita ruutu, jossa sotilas tällä hetkellä on (esim. g2 tai e7)")
print()

queen1 = input("Pelaaja 1 (valkeat): ")
queen2 = input("Pelaaja 2 (mustat): ")

position = Board(queen1, queen2)
correct_board = position.board_setup()
real_position = MakingMoves(position)

while True:
    if not correct_board:
        print("Laiton ruutu kuningattarelle!")
    print()
    print(position.print_board())
    # print(real_position.board.fen)
    # print(real_position.board.unseen_fen)
    print()
    if real_position.turn:
        move = input("Anna siirto (valkean vuoro): ")
        if move == "":
            break
        moving = real_position.make_move(move)
    else:
        move = input("Anna siirto (mustan vuoro): ")
        if move == "":
            break
        moving = real_position.make_move(move)
print("Kiitos pelaamisesta!")


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
