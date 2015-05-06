# Assignment 7: Pandas I
# DS-GA-1007 Programming for Data Science
# Author: Kevin Nguyen
# Created on 4/26/15
# Summary: Class for the program

import unittest
from GapMinder import GapMinder

'''The unit test belows tests the Class for the program.  Because the class performs most of the duties and the user input
of 'year' determines most of the program functioning, we want to test the the viability of these critical elements
of the program.  Again, the unit test requires that both the countries and indicator files be in the same directory.
'''

class RankAndMergeTests(unittest.TestCase):

	def setUp(self):

		'''Loads the files into the program and initializes the GapMinder class.'''

		self.path_countries = "countries.csv"
		self.path_indicators = "indicator gapminder gdp_per_capita_ppp.xlsx"
		self.year = 1880
		self.year2011 = GapMinder(self.path_countries, self.path_indicators, 2011)
		self.year1777 = GapMinder(self.path_countries, self.path_indicators, 1777)

	def test_year(self):

		'''Tests the year once initialized in the class. '''

		self.assertEqual(self.year2011.year, 2011)
		self.assertIn(self.year2011.year, range(1800,2013))
		self.assertNotIn(self.year1777.year, range(1800,2013))

	def test_class(self):

		'''Tests the files to make sure that they are not mixed up, since program relies heavily on indexing during merges,
		it is critical for the files to be in the correct order.
		'''

		self.countries = GapMinder(self.path_countries, self.path_indicators, self.year)
		self.indicators = GapMinder(self.path_countries, self.path_indicators, self.year)
		self.assertIsInstance(self.countries, GapMinder)
		self.assertIsNot(self.countries, self.indicators)
		self.assertNotEqual(self.countries, self.indicators)



if __name__ == '__main__':
	unittest.main()
