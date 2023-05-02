from board import Board
from making_moves import MakingMoves
from unnatural_moves import AbnormalMoves
from database import *
import os

print("Tervetuloa pelaamaan shakin varianttia nimeltä Piilodaami!")
print()
print("Pelin alussa molemmat pelaajat valitsevat yhden sotilaistaan, joka")
print("saakin liikkua kuningattaren tavoin. Kuningatar näyttää kuitenkin")
print("edelleen sotilaalta. Muuten peli noudattaa normaaleja shakin sääntöjä.")
print("Enter lopettaa pelin.")
print("Ohjelma vaatii englanninkielisen shakkinotaation tuntemisen.")
print("(Löytyy takemmista ohjeista)")
print()
instruction = input("Haluatko tarkemmat ohjeet (kyllä tai ei)? ").lower()

if instruction == "kyllä":
    with open("./src/instructions.txt") as file:
        for row in file:
            row = row.replace("\n", "")
            print(row)

print("Valitse yksi sotilaistasi, jonka haluat olevan kunignatar.")
print("Kirjoita ruutu, jossa sotilas tällä hetkellä on (esim. g2 tai e7)")
print()

queen1 = input("Pelaaja 1 (valkeat): ")
queen2 = input("Pelaaja 2 (mustat): ")

position = Board(queen1, queen2)
correct_board = position.board_setup()
real_position = MakingMoves(position)
moves = ""
move_counter = 1

create_table()


def main():
    moves = ""
    move_counter = 1

    while True:
        if not correct_board:
            print("Laiton ruutu kuningattarelle!")
        print()
        print(position.print_board())
        print()
        if real_position.turn:
            move = input("Anna siirto (valkean vuoro): ")
            if move == "":
                break
            os.system('clear')
            moving = real_position.make_move(move)
            moves += f"{move_counter}.{move} "
        else:
            move = input("Anna siirto (mustan vuoro): ")
            if move == "":
                break
            os.system('clear')
            moving = real_position.make_move(move)
            moves += f"{move} "
            move_counter += 1

    player1 = input("Valkeilla pelannut: ")
    player2 = input("Mustilla pelannut: ")
    result = input("Tulos (1-0, 0-1, 0,5-0,5): ")

    save_game(player1, player2, result, moves)
    moves = ""


while True:
    print()
    print("Komennot: ")
    print()
    print("1 - aloittaa uuden pelin")
    print("2 - tulostaa tietokannasta löytyvät pelit")
    print("3 - lopettaa")
    print()
    command = input("Anna komento: ")

    if command == "1":
        main()
    if command == "2":
        print_games()
    else:
        break

print("Kiitos pelaamisesta!")
