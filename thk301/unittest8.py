# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  unittest8.py 
#  April 10,2015
#
#  1. testing input  1990 == 1990
#  2. testing csvReader
#  
###################################

import unittest
import assignment8 as a8
from errorHandler import errorHandlerClass

class Assignment8Test(unittest.TestCase):

    def setUp(self):
        print "setUp"
    
    
    def testInput(self):
        '''
        Testing input
        '''
        self.assertEqual(a8.inputReceiver(1990), 1990)  
        self.assertEqual(a8.inputReceiver(1800), 1800)  
      
      
    def testCountryCsvReader(self):
        '''
        Testing countryCsvReader function
        '''
        thisResult = a8.countryCsvReader('tester.csv')
        Country = thisResult.Country.values
        Region = thisResult.Region.values
        self.assertEqual(Country, 'Test Country')    
        self.assertEqual(Region, 'Test Region')     
        
        
if __name__ == '__main__':
   unittest.main()
   
   