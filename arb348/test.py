'''
This module houses the test code for assignment 8. 

Created on Apr 12, 2015
@author: Adam Biesenbach
'''
import unittest
import os

class Test(unittest.TestCase):

    def testFilesExist(self):
        """ Test to ensure that the output file exist."""
            
        for year in range(2007,2013):
            self.assertTrue(os.path.exists("./IncomeHistogram_"+ str(year)+".pdf"), "A histogram didn't save to output.")
            self.assertTrue(os.path.exists("./LogIncomeHistogram_"+ str(year)+".pdf"), "A histogram didn't save to output.")
            self.assertTrue(os.path.exists("./IncomeBoxplot(log)_"+ str(year)+".pdf"), "A boxplot didn't save to output.")  
        self.assertTrue(os.path.exists("./results.txt"), "Results file doesn't exist.")

if __name__ == "__main__":

    unittest.main()