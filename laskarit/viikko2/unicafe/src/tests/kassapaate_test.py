import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
	def setUp(self):
		self.paate = Kassapaate()
		self.kortti = Maksukortti(1000)
		self.kortti2 = Maksukortti(230)
	
	def test_init_luo_paatteen_oikein(self):
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
		
	def test_init_luo_edullisia_lounaita_ei_myyty(self):
		self.assertEqual(self.paate.edulliset, 0)
		
	def test_init_luo_maukkaita_lounaita_ei_myyty(self):
		self.assertEqual(self.paate.maukkaat, 0)
	
	def test_kateisella_edullinen_riittavasti_rahaa(self):
		self.assertEqual(self.paate.syo_edullisesti_kateisella(250), 10)
		self.assertEqual(self.paate.kassassa_rahaa, 100240)
		self.assertEqual(self.paate.edulliset, 1)
	
	def test_kateisella_edullinen_ei_riittavasti_rahaa(self):
		self.assertEqual(self.paate.syo_edullisesti_kateisella(230), 230)
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
		self.assertEqual(self.paate.edulliset, 0)
		
	def test_kateisella_maukkaasti_riittavasti_rahaa(self):
		self.assertEqual(self.paate.syo_maukkaasti_kateisella(410), 10)
		self.assertEqual(self.paate.kassassa_rahaa, 100400)
		self.assertEqual(self.paate.maukkaat, 1)
	
	def test_kateisella_maukkaasti_ei_riittavasti_rahaa(self):
		self.assertEqual(self.paate.syo_maukkaasti_kateisella(390), 390)
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
		self.assertEqual(self.paate.maukkaat, 0)
	
	
	
	def test_kortilla_edullinen_riittavasti_rahaa(self):
		self.assertEqual(self.paate.syo_edullisesti_kortilla(self.kortti), True)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
		self.assertEqual(self.paate.edulliset, 1)
		
	def test_kortilla_edullinen_ei_riittavasti_rahaa(self):
		self.assertEqual(self.paate.syo_edullisesti_kortilla(self.kortti2), False)
		self.assertEqual(str(self.kortti2), "Kortilla on rahaa 2.30 euroa")
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
		self.assertEqual(self.paate.edulliset, 0)
	
	def test_kortilla_maukkaasti_riittavasti_rahaa(self):
		self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.kortti), True)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
		self.assertEqual(self.paate.maukkaat, 1)
		
	def test_kortilla_maukkaasti_ei_riittavasti_rahaa(self):
		self.assertEqual(self.paate.syo_maukkaasti_kortilla(self.kortti2), False)
		self.assertEqual(str(self.kortti2), "Kortilla on rahaa 2.30 euroa")
		self.assertEqual(self.paate.kassassa_rahaa, 100000)
		self.assertEqual(self.paate.maukkaat, 0)
	
	def test_kortille_ladataan_rahaa(self):
		self.paate.lataa_rahaa_kortille(self.kortti, 100)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 11.00 euroa")
		self.assertEqual(self.paate.kassassa_rahaa, 100100)
	
	def test_kortille_ladataan_negatiivinen_maara_rahaa(self):
		self.paate.lataa_rahaa_kortille(self.kortti, -100)
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
		self.assertEqual(self.paate.kassassa_rahaa, 100000)















	