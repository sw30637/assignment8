# Name: 	test.py
# Author: 	Denis Stukal
# Date: 	April 12, 2015
# Summary:	Provides unit tests for assignment 8
########################################################################################## 

import unittest
import os


class testsForAssignment8(unittest.TestCase):
    '''
    Defines 2 tests: if plots and the results.txt file exit in the working directory
    '''
    def test_plots(self):
        self.assertTrue(os.path.exists('histogram_for_year_2007.pdf'))
        self.assertTrue(os.path.exists('histogram_for_year_2012.pdf'))
        self.assertTrue(os.path.exists('boxplot_for_year_2007.pdf'))
        self.assertTrue(os.path.exists('boxplot_for_year_2012.pdf'))
    
    def test_results_txt(self):
    	self.assertTrue(os.path.exists('results.txt'))
        

if __name__ == '__main__':
	unittest.main()
