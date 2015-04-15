'''
Created on Apr 14, 2015

@author: ds-ga-1007
'''
import pandas as p


def loadCountries():
    '''load csv file and return dataframe'''
    countries = p.read_csv('countries.csv')
    
    return countries

def loadIncome():
    '''load csv file and return dataframe'''
    income = p.read_csv('indicator gapminder gdp_per_capita_ppp.csv').T
    
    print income.head()
    
    return income


