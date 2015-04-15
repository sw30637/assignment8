# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  assignment8.py
#  April 9,2015
#
#  Interactively display Income per person 
#  'Finish' will end the program with 2007-2012 analysis per Regions
#
###################################

import csv
import pandas as pd
from pandas import ExcelFile
import numpy as np
import sys
import matplotlib.pyplot as plt

from errorHandler import errorHandlerClass     #errorHandler.py
from analysis import analysisClass             #analysis.py


def countryCsvReader(thisfile):
    '''
    Reads country csv file, and returns the dataframe
    '''
    with open(thisfile,'r')  as f:
        reader = csv.reader(f)
        headers = next(reader)
        temp_countries=[]
        for row in reader:
            temp_countries.append({'Country': row[0], 'Region':row[1]})
        countries = pd.DataFrame(temp_countries)      #the list becomes DataFrame
        return countries
    
    
def incomeCsvReader(thisfile):
    '''
    Reads income csv file and return the dataframe after rotating and filling the empty value with 0.
    '''
    df = pd.read_excel(thisfile, sheetname='Data', index_col=['gdp pc test'])
    df = df.transpose()        #rotate - years as the rows and countries as the columns
    df = df.fillna(0)          #fill 0
    return df


def inputReceiver(thisInput):
    '''
    Make sure the range of input is between 1800 and 2012.  Detacts other input errors as well
    '''
    try:
        thisInput=int(thisInput)
        if thisInput>2012 or thisInput<1800:
            error = errorHandlerClass("outRange")
            error.errorHandlerFunction() 
        else:
            return thisInput
    except:
        thisError = sys.exc_info()[0]
        error = errorHandlerClass(thisError)
        error.errorHandlerFunction()


def yearGraph(df, thisYear):
    '''
    Graphically display the distribution of income per person across all countries in the world for the given year
    Bar graph is my choice. 
    '''
    graphThis = incomeDF.ix[thisYear]                   #pick out the row (thisYear)
    graphThis= pd.Series(graphThis[(graphThis != 0.)])      #if the value is 0, don't include into graph.  0 = missing data 
    
    fig = plt.figure(figsize=(14,8), dpi=90)
    ax = plt.subplot(111)
    graphThis.plot(kind='bar')
    plt.subplots_adjust(bottom=.2)          
    plt.tick_params(axis='x',  labelsize=5)
    plt.ylabel('Income (GDP per Capita)')
    plt.xlabel('Name of Country') 
    plt.title("The snapshot of the world in %d" %thisYear)
    fig.set_tight_layout(True)
    plt.show()                                          #either display 
    #plt.savefig('Snapshot of %d.png' %thisYear)          #or save  -->this is the only commented-out code 
    
   
    
def merge_by_year(countryDF, incomeDF, thisYear):
    '''​
    merge_by_year(year)​to merge the countries and 
    income data sets for any given year. The result should be a ​DataFrame​ with 
    three columns titled ​Country,​​Region,​and ​Income.​
    '''
    df1 = countryDF         
    df2 = pd.DataFrame(incomeDF.ix[thisYear])
    df2.index.name ="Country"       #give the index a name
    mergedDF = pd.merge(df1, df2, left_on='Country', right_index=True)    #merge on countryDF[Country] and incomeDF.index
    mergedDF =mergedDF.rename(columns={thisYear:'Income'})              #Country,​​Region,​and ​Income
    return mergedDF
    
    
def finishing():
    '''
    when a user finishes, generate graphs for the years 2007­ - 2012
    '''
    for year in xrange(2007, 2013):                            #6 years * 5 regions = 30 PNGs
        mergedDF = merge_by_year(countryDF, incomeDF, year)
        analy = analysisClass(mergedDF, year)
        analy.analysisFunction()
    print "Bye"
    sys.exit(1)
    
    
if __name__ == "__main__":
      thisfile1 ="countries.csv"
      countryDF =  countryCsvReader(thisfile1)
      thisfile2 ="indicator gapminder gdp_per_capita_ppp.xlsx"
      incomeDF =  incomeCsvReader(thisfile2)
      
      while True:
        try:
          thisInput = raw_input("Please type in the year between 1800 to 2012: ")
          
          if (thisInput =="finish") or (thisInput =="Finish") or (thisInput =="FINISH") or (thisInput =="f"):   #calls finishing() 
              finishing()
          elif (thisInput =="quit") or (thisInput =="Quit") or (thisInput =="QUIT") or (thisInput =="q"):  #quit
              print "Bye"
              sys.exit(1)
          else:                                             #otherwise, inputReceiver will check for its value
              thisYear = inputReceiver(thisInput)
              yearGraph(incomeDF, thisYear)  
              
        except:   
            thisError = sys.exc_info()[0]
            error = errorHandlerClass(thisError)
            error.errorHandlerFunction() 

      
