##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 8
#
#	This file contains the main program which will be run
#	It imports all the other modules
#
##############################################################

# Import all the modules for this project
from ExploratoryDataAnalysis import *
from IncomeDistribution import *
from MergeDataFunction import *
from UserInput import *

# Import the built in modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the main function which will give the commands to run the program
if __name__ == '__main__':

	# Read in the datasets as instructed
	countries = pd.read_csv('countries.csv')
	income = pd.read_csv('indicatorgapmindergdp_per_capita_ppp.csv').T
	print income.head()

	# Define a boolean variable which will keep track of the ongoing function
	x = True

	# Start the while loop which will keep keep on asking the user for years
	while (x == True):

		# Call the function which prompts the user to input the year
		# This returns the year which will be analyzed 
		year = TakeUserInput()

		# Set a condition which checks if the user wants to exit
		if year.capitalize() == 'Finish':
			x = False

		# All the analysis functions and class functions
		else:
			DisplayDistribution(year, income)
			ClassAnalysis = DataAnalysis(year)
			ClassAnalysis.Plot_BoxPlots()
			ClassAnalysis.Plot_Histogram()






