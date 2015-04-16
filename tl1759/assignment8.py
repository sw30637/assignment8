###Liwen Tian
#####Assignment8

from analysisclass import analysisclass as anacls 
import pandas as pd 
import numpy as np
from pandas import DataFrame as Df
import matplotlib.pyplot as plt
import math
import sys
import distribution

def merge_by_year(year):
	"merge the two dataframe based on Country"

	data1 = Df(transIncome.ix[year])
	data1 = data1.rename(columns = {year:'Income'})
	data1['Country'] = transIncome.columns
	mergedData = pd.merge(data1,countries,on = ['Country'])
	return mergedData


if __name__ == "__main__":
	print "Let's start with per person income distribution."
	distribution.distributionpcincome()
	print "Now let's do boxplot!"
	countries =  pd.read_csv('countries.csv')
	income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',header = False)
	income.index = income[income.columns[0]]
	transIncome = income.drop(income.columns[0],axis = 1)
	transIncome = transIncome.T
	i = 0
	while True:
		i += 1
		try:

			year = int(raw_input('Please choose a year between 1800 and 2012:'))
			data = merge_by_year(year)
			datacls = anacls(data,year)
			datacls.drawboxplot()

			title = ("Boxplot_by_Region"+str(year)+".pdf")
			plt.savefig(title)
			
		except ValueError:
			print 'You have entered wrong type!'
		except KeyError:
			print 'Make sure the year is between 1800 and 2012!'
		except KeyboardInterrupt:
			print "You have touch the keyboard"
		printstr = raw_input('Go on with another year (yes or no or finish)')
		if printstr == "y" or printstr == 'yes'or printstr == 'Y' or printstr =='Yes':
			continue
		elif printstr == "n" or printstr =='no':
			print 'Quit the program'
			sys.exit()
		elif printstr == 'finish':
			print "The plot has already in the folder"
			sys.exit()
	

