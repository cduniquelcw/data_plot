import unittest

from country_code import get_country_code1,get_country_code2

class Test_country_code(unittest.TestCase):

	def test_country_code1(self):
		out = get_country_code1('China')
		self.assertEqual = (out,'cn')

	def test_country_code2(self):
		out = get_country_code2('United States')
		self.assertEqual = (out,'us')

unittest.main()

