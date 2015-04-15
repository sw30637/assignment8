####Liwen Tian
#####Assignment8

import pandas as pd 
import numpy as np
from pandas import DataFrame as Df
import matplotlib.pyplot as plt
import math
import sys

def distributionpcincome():
	"this function is to explore the per person distribution"
	incomevalue = []
	countries =  pd.read_csv('countries.csv')
	income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',header = False)
	income.index = income[income.columns[0]]
	transIncome = income.drop(income.columns[0],axis = 1)
	transIncome = transIncome.T
	i = 0
	m = True
	while m:
		i += 1
		try:

			year = int(raw_input('Please choose a year between 1800 and 2012:'))
			k = Df(transIncome.ix[year])
			incomevalue = [ele for ele in k[year] if (math.isnan(ele) == False)]
			plt.figure(i)
			plt.subplot(111)
			plt.hist((np.log10(incomevalue)),bins = 20)
			plt.title(str(year) + ' Per person Income Distribution of the World')
			plt.ylabel('Per Person Income \n'+'(log10)')
			title = str(year) +" Income Distribution.pdf"
			plt.savefig(title)
			plt.show(block = False)

		except ValueError:
			print 'You have entered wrong type!'
		except KeyError:
			print 'Make sure the year is between 1800 and 2012!'
		except KeyboardInterrupt:
			print "You have touch the keyboard"
		printstr = raw_input('Go on? (yes or no or finish)')
		if printstr == "y" or printstr == 'yes'or printstr == 'Y' or printstr =='Yes':
			continue
			

		elif printstr == "n" or printstr =='no':
			print "Quit the first step."
			m = False
		elif printstr == 'finish':
			print "See the results in the folder."
			m = False
	return None