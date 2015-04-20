'''
Created by: Joseph Song (JLS731)
Created on: 4/13/2015
Assignment 8
Description: This takes the income per capita dataset and creates a histogram
of the distribution of income per capita for a specific year.
'''

from loaddata import *
import matplotlib.pyplot as plt

def makehistogram(year, incomedata):
    '''Grabs the income per capita data for a specific year'''
    incomedata.ix[year].hist(bins = 50)
    plt.xlabel('Income Per Capita')
    plt.ylabel('Count')
    plt.title('Distribution in year %d' %(year))
    plt.show()
    

