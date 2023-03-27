import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kassassa_alussa_oikein(self):
        rahaa = self.kassa.kassassa_rahaa
        
        self.assertEqual(int(rahaa), 100000)

    def test_maukkaita_alussa_oikein(self):
        maukkaita = self.kassa.maukkaat

        self.assertEqual(maukkaita, 0)

    def test_edullisia_alussa_oikein(self):
        edullisia = self.kassa.edulliset

        self.assertEqual(edullisia, 0)

    def test_kateisella_kassan_raha_nousee_oikein_(self):
        self.kassa.syo_edullisesti_kateisella(240)
        rahaa_kassassa = self.kassa.kassassa_rahaa

        self.assertEqual(rahaa_kassassa, 100240)

    def test_edullisesti_kateisella_palauttaa_rahaa_oikein(self):
        rahaa_takas = self.kassa.syo_edullisesti_kateisella(500)

        self.assertEqual(rahaa_takas, 260)

    def test_maukkaasti_kateisella_kassan_raha_nousee_oikein_(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        kassassa_rahaa = self.kassa.kassassa_rahaa

        self.assertEqual(kassassa_rahaa, 100400)

    def test_maukkaasti_kateisella_palauttaa_rahaa_oikein(self):
        takas_rahaa = self.kassa.syo_maukkaasti_kateisella(500)

        self.assertEqual(takas_rahaa, 100)

    def test_edullisten_maara_kasvaa_ostossa_kateinen(self):
        self.kassa.syo_edullisesti_kateisella(500)
        edullisten_maara = self.kassa.edulliset

        self.assertEqual(edullisten_maara, 1)

    def test_maukkaitten_maara_kasvaa_ostossa_kateinen(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        maukkaitten_maara = self.kassa.maukkaat

        self.assertEqual(maukkaitten_maara, 1)

    def test_edullisesti_kateisella_liian_vahan_rahaa(self):
        takas_rahaa = self.kassa.syo_edullisesti_kateisella(200)

        self.assertEqual(takas_rahaa, 200)

    def test_maukkaasti_kateisella_liian_vahan_rahaa(self):
        takas_rahaa = self.kassa.syo_maukkaasti_kateisella(200)

        self.assertEqual(takas_rahaa, 200)

    def test_kortilla_tarpeeks_rahaa_ja_raha_veloitetaan_oikein_edullisessa(self):
        kortti = Maksukortti(500)
        self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 260)

    def test_kortilla_tarpeeks_rahaa_ja_raha_veloitetaan_oikein_maukkaasti(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 100)

    def test_kortilla_tarpeeks_rahaa_ja_palauttaa_oikean_totuusarvon_edulliset(self):
        kortti = Maksukortti(500)
        totuusarvo = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(totuusarvo, True)

    def test_kortilla_tarpeeks_rahaa_ja_palauttaa_oikean_totuusarvon_maukkaat(self):
        kortti = Maksukortti(500)
        totuusarvo = self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(totuusarvo, True)

    def test_kortilla_tarpeeks_rahaa_ja_myytyjen_maara_kasvaa_edulliset(self):
        kortti = Maksukortti(500)
        self.kassa.syo_edullisesti_kortilla(kortti)
        edullisten_maara = self.kassa.edulliset

        self.assertEqual(edullisten_maara, 1)

    def test_kortilla_tarpeeks_rahaa_ja_myytyjen_maara_kasvaa_maukkaat(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        maukkaitten_maara = self.kassa.maukkaat

        self.assertEqual(maukkaitten_maara, 1)

    def test_kortilla_liian_vahan_rahaa_ja_rahaa_ei_veloiteta_kortilta_edullisesti(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 100)

    def test_kortilla_liian_vahan_rahaa_ja_rahaa_ei_veloiteta_kortilta_maukkaasti(self):
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 100)

    def test_kortilla_liian_vahan_rahaa_ja_myytyjen_maara_ei_kasva_edulliset(self):
        kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(kortti)
        edullisten_maara = self.kassa.edulliset

        self.assertEqual(edullisten_maara, 0)

    def test_kortilla_liian_vahan_rahaa_ja_myytyjen_maara_ei_kasva_maukkaat(self):
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        maukkaitten_maara = self.kassa.edulliset

        self.assertEqual(maukkaitten_maara, 0)

    def test_kortilla_liian_vahan_rahaa_ja_palauttaa_False_totuusarvon_edulliset(self):
        kortti = Maksukortti(100)
        totuusarvo = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(totuusarvo, False)

    def test_kortilla_liian_vahan_rahaa_ja_palauttaa_False_totuusarvon_maukkaat(self):
        kortti = Maksukortti(100)
        totuusarvo = self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(totuusarvo, False)

    def test_kassan_raha_ei_katoa_kortilla_ostettaessa_edulliset(self):
        kortti = Maksukortti(500)
        self.kassa.syo_edullisesti_kortilla
        kassan_raha = self.kassa.kassassa_rahaa

        self.assertEqual(kassan_raha, 100000)

    def test_kassan_raha_ei_katoa_kortilla_ostettaessa_maukkaat(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla
        kassan_raha = self.kassa.kassassa_rahaa

        self.assertEqual(kassan_raha, 100000)

    def test_kortille_ladataan_rahaa_ja_saldo_muuttuu(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 500)
        saldo = kortti.saldo

        self.assertEqual(saldo, 500)

    def test_kortille_ladataan_rahaa_ja_kassan_rahamaara_muuttuu(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 500)
        kassan_rahamaara = self.kassa.kassassa_rahaa

        self.assertEqual(kassan_rahamaara, 100500)

    def test_kortille_ladataan_negatiivinen_summa_ja_saldo_ei_muutu(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, -500)
        saldo = kortti.saldo

        self.assertEqual(saldo, 0)