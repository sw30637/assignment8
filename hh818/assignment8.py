'''
Created on Apr 14, 2015

@author: ds-ga-1007
'''
from fileLoading import *
from incomeDistribution import *
from mergeByYear import *
from dataAnalysis import *

if __name__ == '__main__':
    
    countries = loadCountries()
    income = loadIncome()
    
    while True:
        '''get the user input and make sure it is a valid year i.e. 1800 ~ 2012'''
        year = raw_input('Enter a year between 1800 and 2012')
        
        if year.lower() == 'finish':
            '''print out distributions for 2007 to 2012'''
            years = ['2007', '2008', '2009', '2010', '2011', '2012']
            for year in years:
                print ('printing histogram for ' + year)
                plotDistribution(year, income)
            break
        
        else:
            try:
                if int(year) >= 1800 and int(year) <= 2012:
                    mergedDf = merge_by_year(income, countries, year)
                    #pass year and mergedDf to the dataAnalysis class
                    analysis = dataAnalysis(year, mergedDf)
                    print ('printing boxplot for ' + year)
                    analysis.plotBox()
                    
                else:
                    print ('invalid input')
            except:
                print ('invalid input')
            
                