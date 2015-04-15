

import pandas as pd 
import sys 
import matplotlib.pyplot as plt 

from user_input import *
from analysis import *

import sys
reload(sys)
sys.setdefaultencoding("utf-8")  # cahnge the default encoding


countries = pd.read_csv('countries.csv')

income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', sheetname='Data')
income.rename(columns={'gdp pc test': 'Country'}, inplace=True)

income_trans = income.transpose()
income_trans.columns = list(income_trans.iloc[0])
income_trans.head()


def merge_by_year(year):
	'''Takes a year, generates a dataframe which contains the income data, countries, and region.'''
	merged = pd.merge(countries, income[['Country', year]], on = 'Country', how = 'inner')
	merged.rename(columns={year: 'Income'}, inplace=True)
	merged.set_index('Country')
	return merged



if __name__ == "__main__":


	year = 0
	while True:
		year = get_year()
		if year == 'finish':
			break
		else:
			yeardata = merge_by_year(year)
			plot_year(yeardata)

	print "Generating analysis for 2007-2012"
	for year in range(2007, 2013):
		yeardata = merge_by_year(year)
		analysis = Graph(yeardata, year)
		analysis.plot_boxplot()
		analysis.plot_histogram()
	print "Analysis graphs saved to file."





		

