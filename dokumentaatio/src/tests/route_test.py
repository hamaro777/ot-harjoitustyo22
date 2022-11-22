import unittest
from route import Route

class TestRoute(unittest.TestCase):
	def setUp(self):
		self.reitti = Route("6B", "isatis")

	def test_konstruktori_asettaa_arvot_oikein(self):
		self.assertEqual(str(self.reitti), "6B, isatis")
