# Assignment 8: Pandas I
# DS-GA-1007 Programming for Data Science
# Author: Kevin Nguyen
# Created on 4/26/15
# Summary: Main program for the Income Per Person via the Gapminder Dataset

import sys
reload(sys)
sys.setdefaultencoding('utf8') #This sets utf8 encoding to avoid problems with encoding
from GapMinder import GapMinder
from pylab import *
import warnings
#We want to avoid warnings issues by matplotlib when using plt.tightlayout() so we import warnings
warnings.filterwarnings("ignore")

'''This program give users an opportunity to explore gapminder data on
world Income Per Person (IPP) from 1800 to 2012.  The program ask users for
a year and generates a histgram of that year.  After the user is finished,
the program will generate a graphs from 2007-2012 displaying ranking the top
three against each other (it hopes to invoke thought about the income
disparity between different regions of the world).
'''


if __name__ == "__main__":

    #files must be in the directory of the program with the same name as below
    path_to_countries_file = "countries.csv"
    path_to_indicators_file = "indicator gapminder gdp_per_capita_ppp.xlsx"

    print "Welcome to the world wealth explorer program. We look at \n Income Per Person (i.e. GDP per capital) across the world to measure wealth of the world for a given year. \n The program will generate a graph of the year(s) you wish to explore."
    print "Enter a year between 1800 and 2012"
    print "Enter 'finish' anytime to exit the program." #once user enters finish the program will stop and generate the other graphs

    while True:
        try:
            try:
                year = raw_input ('Enter the year you wish to explore:  ')
                if year == "finish":
                    recentTrends = GapMinder(path_to_countries_file, path_to_indicators_file, 1999)
                    recentTrends.GeneratePlot(2007)
                    recentTrends.GeneratePlot(2008)
                    recentTrends.GeneratePlot(2009)
                    recentTrends.GeneratePlot(2010)
                    recentTrends.GeneratePlot(2011)
                    recentTrends.GeneratePlot(2012)
                    sys.exit()
                elif not int(year): #makes sure that year is inputted as an interger and not word
                    raise TypeError
                elif len(year) != 4: #makes sure that input fits the formate of a four digit year
                    raise TypeError
                elif int(year) < 1800 or int(year) > 2012:
                    print "Year must be between 1800 and 2012"
                else:
                    year = int(year)
                    #here we initialize the GapMinder class
                    recentTrends = GapMinder(path_to_countries_file, path_to_indicators_file, year)
                    countries = recentTrends.loadCountriesCSV()
                    indicators = recentTrends.loadIndicatorsExcel()
                    graphs = recentTrends.plotIncomeByYear()
                    print "graph saved!"
            except ValueError:
                # handle exception and move to outer try-except
                print 'No letters or symbols please! Try again'
            except TypeError:
                print "Invalid input. Try again"
        except KeyboardInterrupt:
            print "Please enter 'finish' to exit the program!"
