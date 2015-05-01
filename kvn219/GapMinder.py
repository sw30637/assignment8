# Assignment 8: Pandas I
# DS-GA-1007 Programming for Data Science
# Author: Kevin Nguyen
# Created on 4/26/15
# Summary: Class for the program

import pandas as pd
from pylab import *
import os
from RankAndMerge import *
import sys

'''GapMinder is the main class for the program.  It handles the loading, processing, merging, graphing and ranking
of the data sets.  The program requires that that the 'countries.csv' and 'indicator gapminder gdp_per_capita_ppp.xlsx' files
are in the directory or the program will not run.'''

class GapMinder(object):

    def __init__(self, path_to_countries_file, path_to_indicators_file, year):
        self.countries_file = path_to_countries_file
        self.indicator_file = path_to_indicators_file
        self.year = year

    def loadCountriesCSV(self):

        '''Loads the countries file.  Assumes that the file is in csv format.'''

        if not os.path.isfile (self.countries_file):
            raise IOError('File does not exist')
        else:
            self.countries = pd.read_csv(self.countries_file, sep=',')
            self.countries = self.countries.set_index('Country')
            return self.countries

    def loadIndicatorsExcel(self):

        '''Loads the indicator file into a pandas dataframe.  Assumes that the file is in excel format.'''

        self.dataset = pd.ExcelFile(self.indicator_file, header=None)
        self.parsed_dataset = self.dataset._parse_excel("Data")
        self.parsed_dataset.rename(columns={'gdp pc test': 'Country'}, inplace=True)
        self.indicators = self.parsed_dataset.set_index('Country')
        return self.indicators

    def setUpData(self):

        '''Sets up the data set by transposing data set, making rows equal to the year.'''

        self.transposed_indicators = self.indicators.transpose()
        return self.transposed_indicators

    def plotIncomeByYear(self):

        '''Plots the world's IPP distribution for a given year.'''

        self.indicators[[self.year]].hist(bins=10)
        plt.ylabel('Frequency (number of countries)')
        plt.xlabel('Income Per Person')
        plt.title(r'Distribution of wealth across the world in ' + str(self.year))
        plt.savefig('Histogram for %s.pdf' % (self.year))

    def mergeDatasets(self):

        '''Merges countries and indicator dataset via index. Assumes that Country is the index for both data sets.'''

        self.merged_dataset = pd.merge(self.countries, self.indicators, left_index=True, right_index=True)
        self.merged_dataset_by_year = self.merged_dataset[['Region', self.year]]
        return self.merged_dataset_by_year

    def ranker(self):

        """Assigns a rank to each country based on IPP, with 1 being the highest country. Assumes the data is sorted in descending order."""

        self.merged_dataset_by_year['region_rankings'] = np.arange(len(self.merged_dataset_by_year)) + 1
        self.ranked_merged_dataset_by_year = self.merged_dataset_by_year
        return self.ranked_merged_dataset_by_year

    def rankedGraph(self):
        
        '''This method graphs the countries ranked in the top three in their reigion against the top 3 in all other reigons in the world.'''
        self.ranked_merged_dataset_by_year.sort(self.year, ascending=False, inplace=True)
        self.graph_ranked_merged_dataset_by_year = self.ranked_merged_dataset_by_year.groupby('Region').apply(ranker)
        self.topThreeByRegion = self.graph_ranked_merged_dataset_by_year[self.graph_ranked_merged_dataset_by_year.region_rankings <= 3].sort(self.year)
        self.topThreeByRegion.plot(kind="barh", legend=None)
        plt.ylabel('Frequency (number of countries)')
        plt.xlabel('Income Per Person')
        plt.title(r'Ranking The Top 3 in Each Region Against One Another in ' + str(self.year))
        plt.tight_layout()
        plt.savefig('How_the_Top_Three_Incomes_In_Each_Region_Rank_Against_Each_Other%s.pdf' % (self.year))

    def GeneratePlot(self, year):
        
        '''This method runs the other methods in the class in the sequence needed for the program to work.'''
        self.year = year
        self.loadCountriesCSV()
        self.loadIndicatorsExcel()
        self.mergeDatasets()
        self.ranker()
        self.rankedGraph()
        self.plotIncomeByYear()

if __name__ == "__main__":

    path_to_countries_file = "countries.csv"
    path_to_indicators_file = "indicator gapminder gdp_per_capita_ppp.xlsx"
    year = 1888

    print "\n"
    print "Question 1"
    print "Preview of countries data set"
    print "\n"
    User = GapMinder(path_to_countries_file, path_to_indicators_file, year)
    User.loadCountriesCSV()
    print User.countries.head()
    print "\n"
    print "Question 2"
    print "Preview of indicator data set"
    User.loadIndicatorsExcel()
    print User.indicators.head()
    print "\n"
    print "Question 3"
    print "Preview of transposed indicator data set"
    print "\n"
    User.setUpData()
    print User.transposed_indicators.head()
    sys.exit()



