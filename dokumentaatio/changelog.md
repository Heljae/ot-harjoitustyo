# Changelog
## Viikko 3
- Luokka LegalMoves tarkistaa lähes kaikkien nappuloitten lailliset siirrot annetussa ruudussa. Lähetti vielä puuttuu.
- Lisätty luokka Board, joka luo uuden laudan aloitusasemasta. Luokassa on metodi print_board(), joka palauttaa shakkilaudan printattavassa muodossa.

## Viikko 4
- Luokka LegalMoves. Nyt luokka tarkistaa jokaisen nappulan laillisen siirron sotilaan lyöntejä ja erikoissiirtoja lukuunottamatta.  
- Luokassa Board on nyt metodi board_without_icons_and_dots, joka palauttaa laudan siten, että tyjät ruudut ovat ykkösiä. Lauta on edelleen printattavassa muodossa.  
- Luokassa Board on metodi new_fen, joka palauttaa uuden FEN muotoisen shakkilaudan, jossa on tehty metodille annettava siirto.  
- Luotiin luokka MakingMoves, jossa on jokaiselle shakkinappulalle oma piilotettu metodi, jota metodi make_move kutsuu nappulaa siirrettäessä. Metodi make_move palauttaa uuden aseman FEN muodossa. Tällä hetkellä vain tornilla on kapseloitu metodi.  
- Luotiin hidden_queen_main.py tiedostoon alustava käyttöliittymän rakenne  
- Luotiin tiedosto main_inputs.py, joka ei toistaiseksi tee mitään järkevää  
 
## Viikko 5
- Muokattiin luokkaa Board toimivaksi (new_fen toimii)  
- Board luokassa metodi board_setup, joka asettaa kaksi annettua kuningatarta laudalle siten, että pelaajat eivät kuitenkaan näe niitä  
- Board luokassa pystyy nyt muokkaamaan asemaa, jota pelaajat eivät näe  
- main tiedosto huomattavasti erilainen  
- Nappuloiden liikuttaminen erilainen, toistaiseksi mustilla ei voi tehdä siirtoja :')  
- Muokattiin luokkia makingmoves, Board ja LegalMoves  
- Ohjelma toimii jotenkin ja nyt ohjelmalle voi antaa kaksi kuningatarta  
- Nappuloiden lyöminen ei toimi halutulla tavalla  

## Viikko 6
- Lisättiin tarkemmat ohjeet shakkinotaatiolle.  
- Pelejä pystyy nyt lisäämään tietokantaan  
