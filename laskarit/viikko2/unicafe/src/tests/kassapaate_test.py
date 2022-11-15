import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_oikea_alkusaldo(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_oikea_alku_edullinen(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_oikea_alku_maukas(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_varat_kasvaa_kateisostolla_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(1000)
        
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_oikea_vaihtoraha_kateisostolla_edullinen(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(1000)
        
        self.assertEqual(vaihtoraha, 760)

    def test_kateisen_taytyy_riittaa_lounaiden_maara_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(10)

        self.assertEqual(self.kassa.edulliset, 0)

    def test_kateisen_taytyy_riittaa_vaihtoraha_edullinen(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(10)

        self.assertEqual(vaihtoraha, 10)  

    def test_kateisen_taytyy_riittaa_kassaraha_ei_muutu_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(10)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    #maukas käteinen

    def test_varat_kasvaa_kateisostolla_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(1000)
        
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_oikea_vaihtoraha_kateisostolla_maukas(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(1000)
        
        self.assertEqual(vaihtoraha, 600)

    def test_kateisen_taytyy_riittaa_lounaiden_maara_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(10)

        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisen_taytyy_riittaa_vaihtoraha_maukas(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(10)

        self.assertEqual(vaihtoraha, 10)  

    def test_kateisen_taytyy_riittaa_kassaraha_ei_muutu_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(10)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    #edullinen korttiosto

    def test_varat_ei_kasva_korttiostolla_edullinen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_summa_veloitetaan_kortilta_korttiosto_edullinen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 760)

    def test_korttiveloitus_palauttaa_true_edullinen(self):
        palaute = self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(palaute, True)

    def test_myytyjen_maara_kasvaa_kortilla_edullinen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassa.edulliset, 1)

    def test_rahaton_kortti_ei_veloiteta_edullinen(self):
        kortti = Maksukortti(1)
        self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 1)

    def test_rahaton_kortti_ei_lounaskasvua_edullinen(self):
        kortti = Maksukortti(1)
        self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassa.edulliset, 0)

    def test_rahaton_kortti_palauttaa_false_edullinen(self):
        kortti = Maksukortti(1)
        palaute = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(palaute, False)

    # kortti maukas

    def test_varat_ei_kasva_korttiostolla_maukas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_summa_veloitetaan_kortilta_korttiosto_maukas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 600)

    def test_korttiveloitus_palauttaa_true_maukas(self):
        palaute = self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(palaute, True)

    def test_myytyjen_maara_kasvaa_kortilla_maukas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassa.maukkaat, 1)

    def test_rahaton_kortti_ei_veloiteta_maukas(self):
        kortti = Maksukortti(1)
        self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 1)

    def test_rahaton_kortti_ei_lounaskasvua_maukas(self):
        kortti = Maksukortti(1)
        self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassa.maukkaat, 0)

    def test_rahaton_kortti_palauttaa_false_maukas(self):
        kortti = Maksukortti(1)
        palaute = self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(palaute, False)

    def test_rahan_lataaminen_kasvattaa_korttia(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)

        self.assertEqual(self.kortti.saldo, 1100)

    
    def test_rahan_lataaminen_pienentaa_kassaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_negatiivinen_lataussumma_ei_kasvata_kassaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -3301391203910239)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_negatiivinen_lataussumma_ei_kasvata_korttia(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -14709178290184)

        self.assertEqual(self.kortti.saldo, 1000)
    