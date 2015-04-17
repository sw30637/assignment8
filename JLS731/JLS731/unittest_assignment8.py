'''
Created by: Joseph Song (JLS731)
Created on: 4/16/2015
Assignment 8
Description: This is the unit test to test the package to make sure the
programs are working properly.
'''
# Import modules
from loaddata import *
from mergedataframes import *
from makehistogram import *
from exploratorytools import *
import unittest
import os.path

class Test(unittest.TestCase):


    def testdataload(self):
        '''Test to make sure the size of the data are correct'''

        #The correct shapes
        self.trueincomeshape = (213,259)
        self.truecountryshape = (194,2)
        self.truemergeshape = (177,3)

        #The shapes of the data being outputted
        self.testcountry = loadcsvdata('countries.csv')
        self.testincome = loadxlsxdata('indicator gapminder gdp_per_capita_ppp.xlsx')
        self.testcountryshape = loadcsvdata('countries.csv').shape
        self.testincomeshape = loadxlsxdata('indicator gapminder gdp_per_capita_ppp.xlsx').shape
        self.testmergeshape = merge_by_year(2002, self.testincome, self.testcountry).shape

        self.assertEqual(self.testcountryshape, self.truecountryshape, "Incorrect Size")
        self.assertEqual(self.testincomeshape, self.trueincomeshape, "Incorrect Size")
        self.assertEqual(self.testmergeshape, self.truemergeshape, "Incorrect Size")
    
    def testfileexist(self):
        '''Test to make sure that the boxplot and histogram files exist'''
        self.assertTrue(os.path.exists("./boxplot2007.pdf"), "The output does not exists")
        self.assertTrue(os.path.exists("./histogram2007.pdf"), "The output does not exists")
        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
