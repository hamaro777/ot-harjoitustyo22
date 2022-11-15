import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.10 euroa")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_ei_saldoa(self):
        self.maksukortti.ota_rahaa(100000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_true_jos_rahaa(self):
        vastaus = self.maksukortti.ota_rahaa(500)

        self.assertEqual(vastaus, True)

    def test_metodi_palauttaa_False_jos_ei_rahaa(self):
        vastaus = self.maksukortti.ota_rahaa(100000)

        self.assertEqual(vastaus, False)