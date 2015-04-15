##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 8
#
#	This file will check if all the modules are present in the package for the program to run properly
#
#
##############################################################

import unittest
import os


class testForModules(unittest.TestCase):

	def testCompletePackage(self):

		# Check for all the files needed in the Python Package
		self.assertTrue(os.path.exists('assignment8.py'))
		self.assertTrue(os.path.exists('IncomeDistribution.py'))
		self.assertTrue(os.path.exists('ExploratoryDataAnalysis.py'))
		self.assertTrue(os.path.exists('UserInput.py'))
		self.assertTrue(os.path.exists('MergeDataFunction.py'))
		self.assertTrue(os.path.exists('__init__.py'))

		# Check for the results.txt
		self.assertTrue(os.path.exists('results.txt'))

if __name__ == '__main__':
	unittest.main()