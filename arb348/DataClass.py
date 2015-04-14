'''
The class which combines the country data and the income data, and also has a number of 
other useful methods for use in the other parts of the problem set. 

Created on Apr 10, 2015
@author: Adam Biesenbach
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from MergeByYear import merge_by_year

class CountryData(object):
    '''
    A Class to combine the country datasets and provide some 
    reusable methods to use on data of this type. 
    '''

    def __init__(self, year):
        """We need to pull in the year for this particular instance of this class."""
        self.year=int(year)
        self.countries = pd.read_csv('countries.csv')
        self.income = pd.read_excel('gdp_per_capita_ppp.xlsx', 0, index_col=None, na_values=['NA'])
        
        # Make countries the row index. the dataset here has columns as incomes, rows as countries.
        self.income.index=self.income[self.income.columns[0]] 
        self.income = self.income.drop(self.income.columns[0], axis = 1)
        
        # Convert years from floats to ints. Here map() applies the lambda function to 
        # all the members of the income column headers, which are the years. 
        self.income.columns = map(lambda x: int(x), self.income.columns) 

        # The program transforms the data to have 
        # years as the rows and countries as the columns.
        self.income = self.income.transpose()
        
        # Print this dataset whenever it is loaded.
        print self.income.head()

    def CreateBoxPlots(self):
        """Generates a set of pdf files
        containing boxplots and histograms."""
        self.JoinedDatasets = merge_by_year(self)
        self.JoinedDatasets.boxplot('Income', by = 'Region', rot = 20)
        plt.title("Year:" + str(self.year))
        plt.ylabel('Income/person (log scale)')
        plt.ylim(10**2, 10.5 **5)
        plt.yscale('log')
        title = "IncomeBoxplot(log)_" + str(self.year)+".pdf"
        plt.savefig(title) 
        plt.close()

    def CreateHistograms(self):
        """ Display the distribution of income per person
        across all the countries for the given year. Choose the 
        best kind of plot to display this data.  Here, I used a histogram. """
        plt.plot(subplots=True)
        plt.hist(self.income.ix[self.year].dropna().values, bins = 25)
        plt.title('Year: %i' % self.year)
        plt.xlabel('Income/person')
        plt.ylabel('Frequency')
        title = "IncomeHistogram_" + str(self.year)+".pdf"
        plt.savefig(title) 
        plt.close()
            
        plt.hist(np.log10(self.income.ix[self.year].dropna().values), bins = 25)
        plt.title('Year: %i' % self.year)
        plt.xlabel('Income/person (log scale)')
        plt.ylabel('Frequency')
        title = "LogIncomeHistogram_" + str(self.year)+".pdf"
        plt.savefig(title) 
        plt.close()
    