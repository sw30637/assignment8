# Name: 	dataClass.py
# Author: 	Denis Stukal
# Date: 	April 12, 2015
# Summary:	Defines Data class
########################################################################################## 


import pandas as p
from assignment8Functions import assignment8Exceptions as ex

class Data:
    '''
    A Data class object has 2 attributes with data: countries and income.
    merge_by_year() takes year as input produces a merged data set from self.countries and self.income. 
    Possible exceptions in merge_by_year() are KeyError and ValueError if wrong data set are loaded. 
    '''
    def __init__(self):
        '''
        Initializes an instance of the class by loading country and income data into class attributes as pandas DataFrame 
        '''
        self.countries = self.loadContryData()
        self.income = self.loadIncomeData()


    def loadContryData(self):
        '''
        No-argument function that loads countries.csv data and returns a pandas DataFrame.
        IOError if no countries.csv in the current directory. 
        ValueError if the wrong file is used. 
        '''
        try:
            return p.read_csv('countries.csv', header=0)
        except IOError, ValueError:
            raise ex.WrongInput()


    def loadIncomeData(self):
        '''
        No-argument function that loads indicator gapminder gdp_per_capita_ppp.xlsx data 
        and returns a pandas DataFrame with countries in columns and years in rows. 
        Shows a head of the DataFrame after loading it. 
        IOError if no indicator gapminder gdp_per_capita_ppp.xlsx in the current directory. 
        ValueError if the wrong file is used. 
        '''
        try: 
            income = p.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', header=0)
            # Reshape income data
            income = income.transpose()
            # Get column names 
            income.columns = income.ix[0]
            # Get rid of a superfluous row
            income = income.drop(income.index[0], axis=0)
            print 'Loading income data'
            print income.head()
            return income
        except IOError, ValueError:
            raise ex.WrongInput()

    def mergeByYear(self, year):
        '''
        Integer between 1800 and 2012 as input. Returns a pandas DataFrame with merged self.countries and self.income
        KeyError and ValueError if wrong files are used. 
        '''
        try:
            incomeSelectedYear = p.DataFrame({'countries': self.income.columns.values, 'income': self.income.ix[year]})
            mergedDF = incomeSelectedYear.merge(self.countries, left_on = 'countries', right_on = 'Country').drop(['Country'], axis=1)
            mergedDF.columns = ['Country', 'Income', 'Region']
            mergedDF = mergedDF.reindex(columns = ['Country', 'Region', 'Income'])
            mergedDF['Income'] = mergedDF['Income'].astype(float)
            return mergedDF  
        except KeyError, ValueError:
            raise ex.WrongInput()


