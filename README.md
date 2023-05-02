# Piilodaami
Projektissa on lopulta mahdollista pelata shakin erästä varianttia nimeltä piilodaami. Variaatiossa molemmat pelaajat valitsevat yhden sotilaistaan ja tämä sotilas saa pelin aikana liikkua kuningattaren tavoin, vaikka nappula näyttääkin sotilaalta.

## Dokumentaatio
[vaatimusmaarittely](https://github.com/Heljae/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
[tuntikirjanpito](https://github.com/Heljae/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)  
[changelog](https://github.com/Heljae/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Sovelluksen asennus
1. Asenna riippuvuudet seuraavalla komennolla:  
```bash
poetry install
```
2. Ohjelma käynnistyy komennolla:  
```bash
poetry run invoke start
```

## Komentoja komentoriville
### Ohjelman suorittaminen
Seuraava komento suorittaa ohjelman:
```bash
poetry run invoke start
```

### Ohjelman testaus
Ohjelman testit voidaan suorittaa komennolla:
```bash
poetry run invoke test
```

### Testikattavuus
Ohjelmalle voi luoda testikattavuusraportin seuraavalla komennolla. Komento luoo raportin htmlcov-hakemistoon.
```bash
poetry run invoke coverage-report
```

### Pylint
Seuraava komento suorittaa tiedoston .pylintrc määrittelemät tarkistukset.
```bash
poetry run invoke lint
```

## Release
Uusin release löytyy [tästä](https://github.com/Heljae/ot-harjoitustyo/releases/tag/viikko6).  
  
Viikon 5 [release](https://github.com/Heljae/ot-harjoitustyo/releases/tag/viikko5)  
Viikon 6 [release](https://github.com/Heljae/ot-harjoitustyo/releases/tag/viikko6)

