# Projektin tämänhetkisiä ongelmia ja puutteita
## Luokka Board
- new_fen metodi toimii vain kun metodi saa aseman alkuasemasta (joshtuu siitä, että range liian suuri)  

## Luokka MakingMoves
- Kaikki nappulat voivat liikkua toistensa läpi  
- Nappulat voivat syödä omanvärisiä nappuloita  
- Jos kaksi samaa nappulaa voi siirtyä samaan ruutuun, koodi siirtää satunnaisesti toista  
- Mitä jos nappulaa yrittää siirtää ruutuun, jossa se on jo?  
- Sotilaiden siirtäminen ei toimi, koska metodi ei näe edellistä ruutua laillisissa siirroissa  
- 

## Luokka LegalMoves
- Toimii oikein!  
- Mahdollisia ruutuja tosin melko paljon jokaisessa asemassa
