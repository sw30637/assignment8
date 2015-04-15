'''
Created on Apr 14, 2015

@author: ds-ga-1007
'''
import pandas as p

def merge_by_year(income, countries, year):
    '''merge two data sets by country names, and have three columns: Country, Region, and Income'''
    tempDf = p.DataFrame({'Country':income.ix['gdp pc test'], "Income":income.ix[year]})
    mergedDf = p.merge(countries, tempDf, on = 'Country', how='inner')
    
    return mergedDf