'''
Created on Apr 14, 2015

@author: ds-ga-1007
'''
import matplotlib.pyplot as plt

def plotDistribution(year, dataframe):
    '''take a year and dataframe and plot histogram'''
    plt.hist(dataframe.ix[year].dropna().values, bins = 50)
    plt.title('Income Distribution for year ' + year)
    plt.xlabel('Income Per Person')
    plt.ylabel('Frequency')
    
    fileName = year + 'IncomeDistribution.pdf'
    plt.savefig(fileName)
    plt.clf()
    
