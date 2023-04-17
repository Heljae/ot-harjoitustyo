# Changelog
## Viikko 3
- Luokka LegalMoves tarkistaa lähes kaikkien nappuloitten lailliset siirrot annetussa ruudussa. Lähetti vielä puuttuu.
- Lisätty luokka Board, joka luo uuden laudan aloitusasemasta. Luokassa on metodi print_board(), joka palauttaa shakkilaudan printattavassa muodossa.

## Viikko 4
- Luokka LegalMoves. Nyt luokka tarkistaa jokaisen nappulan laillisen siirron sotilaan lyöntejä ja erikoissiirtoja lukuunottamatta.  
- Luokassa Board on nyt metodi board_without_icons_and_dots, joka palauttaa laudan siten, että tyjät ruudut ovat ykkösiä. Lauta on edelleen printattavassa muodossa.  
- Luokassa Board on metodi new_fen, joka palauttaa uuden FEN muotoisen shakkilaudan, jossa on tehty metodille annettava siirto.  
- Luotiin luokka MakingMoves, jossa on jokaiselle shakkinappulalle oma kapseloitu metodi, jota metodi make_move kutsuu nappulaa siirrettäessä. Metodi make_move palauttaa uuden aseman FEN muodossa. Tällä hetkellä vain tornilla on kapseloitu metodi.  
