import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")
    
    def test_return_ota_rahaa_alle_saldo(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
    
    def test_saldo_ota_rahaa_alle_saldo(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_return_ota_rahaa_yli_saldo(self):
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)
    
    def test_saldo_ota_rahaa_yli_saldo(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")