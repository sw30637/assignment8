'''
The merge function for assignment 8. 

Created on Apr 12, 2015
@author: Adam Biesenbach
'''

import pandas as pd

def merge_by_year(DataInstance):
    """ Merge country and income data sets by year.
    the results should be a dataframe with three columns 
    titled Country, Region, and Income. """
    
    # Create a DF from the income dataset, The original dataset has countries as column headers 
    # with incomes per person down the columns, and years for the rows. the ix command 
    # to pull out the rows for the year submitted by the user. 
    data = pd.DataFrame(DataInstance.income.ix[DataInstance.year].values, columns = ['Income'])    

    # Here we assign the name "Country" to country names from the income file, and add it as a column to the 'data' file. 
    data['Country'] = DataInstance.income.columns

    # perform the inner join of the countries and income datasets. The inner join
    # is the intersection of the two datasets. 
    joined = pd.merge(data, DataInstance.countries, how="inner", on=['Country'])
    return pd.DataFrame(joined)