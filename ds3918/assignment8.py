# Name: 	assignment8.py
# Author: 	Denis Stukal
# Date: 	April 12, 2015
# Summary:	Loads country/region and income data, prompts the user to enter a year, merges data for that year
# 			and saves boxplots for income by region for that year.
########################################################################################## 

import sys
import pandas as p
from assignment8Functions.dataModule import dataClass
from assignment8Functions import inputChecker, exploreGraphs, produceOutput
from assignment8Functions import assignment8Exceptions as ex

if __name__ == '__main__':
    # Instantiate a Data class object, loading the data
    myData = dataClass.Data()

    # Infinite loop interrupted by 'finish' only
    while True:
        try: 
            inputYear = raw_input('What year do you want to look at (from 1800 to 2012)? ')
            
            if inputYear == 'finish':
                print 'Producing graphs for 2007 - 2012 and exiting the program'
                # Produce graphs for 2007 - 2013 if user typed "finish"
                for year in range(2007, 2013, 1):
                    produceOutput.makeOutput(myData, year)
                sys.exit(0)
            
            elif not inputChecker.isInputNumeric(inputYear):
                print "Wrong input. Please, input a year between 1800 and 2012\n"
                continue
            
            else:
                # Make input numeric
                inputYear = int(inputYear)
                # Check if input is between 1800 and 2012
                if not inputChecker.isInputRightInterval(inputYear):
                    print "Input year should be between 1800 and 2012\n"
                    continue
                produceOutput.makeOutput(myData, inputYear)
        except KeyboardInterrupt:
            print 'Enter "finish" to exit the program\n'
            continue
        except ex.WrongInput:
        	print 'WrongInput exception. Exiting the program'
        	sys.exit(1)