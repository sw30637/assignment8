'''
Created by: Joseph Song (JLS731)
Created on: 4/13/2015
Assignment 8
Description: This module merges the "country" data with the "income" data.
It returns a dataframe dataset of country names, regions, income per capita.
'''

import pandas as pd
from loaddata import *

def merge_by_year(year, incomedata, countrydata):
    '''This function merges the country and income data'''
    incomebyyear = incomedata.ix[year].reset_index()
    mergeddata = pd.merge(incomebyyear,countrydata)
    mergeddata.rename(columns={year: 'Income'}, inplace = True)
    return mergeddata


