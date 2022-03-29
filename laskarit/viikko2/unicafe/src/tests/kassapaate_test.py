import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(500)
    
    def test_init_raha_oikein(self):
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
    
    def test_init_edulliset_oikein(self):
        self.assertEqual(self.paate.edulliset, 0)
    
    def test_init_maukkaat_oikein(self):
        self.assertEqual(self.paate.maukkaat, 0)
    
    def test_kateismaksu_on_riittava_edullinen(self):
        self.paate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 100240)
        self.assertEqual(self.paate.edulliset, 1)
    
    def test_kateismaksu_on_riittava_maukas(self):
        self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 100400)
        self.assertEqual(self.paate.maukkaat, 1)
    
    def test_korttimaksu_edullinen(self):
        ret = self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.paate.edulliset, 1)
        self.assertEqual(str(self.kortti), "saldo: 2.6")
        self.assertEqual(ret, True)

    def test_korttimaksu_maukas(self):
        ret = self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.paate.maukkaat, 1)
        self.assertEqual(str(self.kortti), "saldo: 1.0")
        self.assertEqual(ret, True)
    
    def test_kateismaksu_ei_riittava_edullinen(self):
        self.paate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kateismaksu_ei_riittava_maukas(self):
        self.paate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_kortti_ei_riittava_maukas(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        ret = self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(ret, False)
        self.assertEqual(self.paate.maukkaat, 1)
    
    def test_kortti_ei_riittava_edullinen(self):
        self.paate.syo_maukkaasti_kortilla(self.kortti)
        ret = self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(ret, False)
        self.assertEqual(self.paate.edulliset, 0)
    
    def test_lataa_rahaa_neg(self):
        self.paate.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(str(self.kortti), "saldo: 5.0")
    
    def test_lataa_rahaa(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(str(self.kortti), "saldo: 15.0")
