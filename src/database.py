import sqlite3

db = sqlite3.connect("games.db")
db.isolation_level = None


def create_table():
    try:
        db.execute('''
        CREATE TABLE Games (
        id INTEGER PRIMARY KEY,
        player1 TEXT,
        player2 TEXT,
        result TEXT,
        moves TEXT)
        ''')
    except:
        pass


def save_game(player1, player2, result, moves):
    # Saves games into the database

    db.execute('''
    INSERT INTO Games
    (player1, player2, result, moves)
    VALUES (?, ?, ?, ?)
    ''', [player1, player2, result, moves])


def search_game():
    pass


def print_games():
    # prints between who the game was and the result

    games = db.execute('''
    SELECT *
    FROM Games
    ''').fetchall()

    output = ""

    for game in games:
        output += f"{game[0]} Pelaajat: {str(game[1])}-{str(game[2])}, Tulos: {game[3]}\n"

    print(output)
