# Assignment 8: Pandas I
# DS-GA-1007 Programming for Data Science
# Author: Kevin Nguyen
# Created on 4/26/15
# Summary: module that merges the data sets and graphs performs exploratory data analysis on the data set.

import pandas as pd
from pylab import *
from GapMinder import *

'''This python module contains the mergeDatasets, ranker, and rankedGraph functions for the program'''

def mergeDatasets(countries, indicators, year):

    '''Merges countries and indicator data set via index. Assumes that Country is the index for both data sets.'''

    merged_dataset = pd.merge(countries, indicators, left_index=True, right_index=True)
    merged_dataset_by_year = merged_dataset[['Region', year]]
    return merged_dataset_by_year

def ranker(merged_dataset_by_year):

    """Assigns a rank to each country based on IPP, with 1 being the highest country. Assumes the data is sorted in descending order."""

    merged_dataset_by_year['region_rankings'] = np.arange(len(merged_dataset_by_year)) + 1
    ranked_merged_dataset_by_year = merged_dataset_by_year
    return ranked_merged_dataset_by_year

def rankedGraph(ranked_merged_dataset_by_year, year):

    '''Graphs the top ranked countries in each region against one another in a overarching graph /n this allows the user to see income disparity among the different regions'''

    ranked_merged_dataset_by_year.sort(year, ascending=False, inplace=True) #sorts the data set
    graph_ranked_merged_dataset_by_year = ranked_merged_dataset_by_year.groupby('Region').apply(ranker) #ranks the data set and uses the ranker function from the RankAndMerge module
    topThreeByRegion = graph_ranked_merged_dataset_by_year[graph_ranked_merged_dataset_by_year.region_rankings <= 3].sort(year) #takes the top three countries from each region
    topThreeByRegion.plot(kind="barh", legend=None)
    plt.ylabel('Frequency (number of countries)')
    plt.xlabel('Income Per Person')
    plt.title(r'Ranking The Top 3 in Each Region Against One Another in ' + str(year))
    plt.tight_layout()
    plt.savefig('How_the_Top_Three_Incomes_In_Each_Region_Rank_Against_Each_Other.pdf')

if __name__ == "__main__":
    path_to_countries_file = "countries.csv"
    path_to_indicators_file = "indicator gapminder gdp_per_capita_ppp.xlsx"

    #Question 5
    year = 2000
    User = GapMinder(path_to_countries_file, path_to_indicators_file, year)
    countries = User.loadCountriesCSV()
    indicators = User.loadIndicatorsExcel()

    merged_dataset = mergeDatasets(countries, indicators, year)
    print merged_dataset.head()
