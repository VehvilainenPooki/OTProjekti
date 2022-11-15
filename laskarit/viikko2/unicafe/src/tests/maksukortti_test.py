import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
	def setUp(self):
		self.kortti = Maksukortti(1000)

	def test_luotu_kortti_on_olemassa(self):
		self.assertNotEqual(self.kortti, None)
		
	def test_konstruktori_asettaa_saldon_oikein(self):
		self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
		
	def test_kortille_voi_ladata_rahaa(self):
		self.kortti.lataa_rahaa(2500)

		self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")
		
	def test_kortilta_voi_ottaa_rahaa(self):
		self.kortti.ota_rahaa(1000)

		self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.00 euroa")
		
	def test_kortilta_ei_voi_ottaa_liikaa_rahaa(self):
		self.kortti.ota_rahaa(1100)

		self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
		
	def test_rahan_ottaminen_palauttaa_true(self):
		self.assertEqual(self.kortti.ota_rahaa(900), True)
	
	def test_liian_rahan_ottaminen_palauttaa_false(self):
		self.assertEqual(self.kortti.ota_rahaa(1100), False)