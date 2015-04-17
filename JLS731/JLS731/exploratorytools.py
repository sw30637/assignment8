'''
Created by: Joseph Song (JLS731)
Created on: 4/13/2015
Description: Creates a class for producing exploratory charts (boxplots and histograms) of the income per capita data
by region.
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mergedataframes import *

class exploratorytools:
    
    def __init__(self, year, incomedata, countrydata):
        '''This is the exploratoryTools class'''
        self.year = year
        self.incomedata = incomedata
        self.countrydata = countrydata
        self.data = merge_by_year(self.year, self.incomedata, self.countrydata)
        
    def makehistogram(self):
        '''Create a histogram of income per capita by region'''
        self.data.hist(by = 'Region', bins = 10, sharex = True, sharey = True, xlabelsize = 10, ylabelsize = 10)
        plt.suptitle('Distribution of Income Per Capita by Regions in year %d, X-axis: Income Per Capita, Y-Axis: Count' %(self.year))
        filename = 'histogram'+str(self.year)+'.pdf'
        plt.savefig(filename)
        plt.show()
        


    def makeboxplot(self):
        '''Create a boxplot of the income per capita by region'''
        self.data.boxplot('Income', by = 'Region', fontsize = 10)
        plt.xlabel('Region')
        plt.ylabel('Income Per Capita')
        plt.ylim((0,100000))
        plt.title('Distribution of income per capita by region in year %d' %(self.year))
        plt.suptitle('')
        filename = 'boxplot'+str(self.year)+'.pdf'
        plt.savefig(filename)
        plt.show()
        
