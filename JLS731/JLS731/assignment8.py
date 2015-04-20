'''
Created by: Joseph Song (JLS731)
Created on: 4/14/2015
Assignment 8
Description: This is the main program to run assignment #8.
It loads the datasets, takes user input (year), and displays the 
histogram from question 4 and also the "exploratory data analysis tools".

Note that this is a little different from the way the problem is
posed in the assignment. The assignment suggests that it only show
the graph from question 4 and then once the user types "finish" produce
the "exploratory analysis tools" for 2007 to 2012.

I decided to produce all the charts as the user inputs years. 
'''

# Import modules
from loaddata import *
from mergedataframes import *
from makehistogram import *
from exploratorytools import *
import matplotlib.pyplot as plt


if __name__ == '__main__':

    # Load Datasets and present the "head" of the income dataframe
    countries = loadcsvdata('countries.csv')
    income = loadxlsxdata('indicator gapminder gdp_per_capita_ppp.xlsx')
    print income.head()

    # Boolean variable to toggle on/off as user input changes
    trigger = False    

    # User input and catch exceptions
    while(trigger == False):
        try:
            userinput = raw_input("Enter a four digit year between 1800 and 2012 or finish to end program: " + '\n')            
            if userinput.lower() == "finish":
                trigger = True
            else: 
                year = int(userinput)
                assert(1800 <= year <= 2012)
                chart1 = makehistogram(year, income)
                regiondata = exploratorytools(year, income, countries)
                regiondata.makehistogram()
                regiondata.makeboxplot()
        except KeyboardInterrupt:
            print("Keyboard interrupt received: Good Bye")
            trigger = True
        except:
            print("Incorrect input, please type a 4-digit year between 1800 and 2012")

    print("Program Complete: Good Bye")
