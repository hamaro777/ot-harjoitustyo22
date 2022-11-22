import unittest
from user import User


class TestUser(unittest.TestCase):
	def setUp(self):
		self.kayttaja = User("woosa", "uwu")

	def test_konstruktori_asettaa_nimen_oikein(self):
		self.assertEqual(str(self.kayttaja), "woosa, uwu")
