##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 8
#
#	This file contains the function to display the data for the income distribution for all the countries
#	It takes in the dataset income and displays a histogram for income per percon for a specified year
#
##############################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def DisplayDistribution(year, dataset):

	# Put a try/except to check if the dataset is correct
	try:
		# Plot the histogram for the given year for the distribution of income per person for all the countries
		plt.hist(dataset.ix[year].dropna().values,bins=20)
		plt.title("This is the Income Distribution for the year "+year+" across all countries")
		plt.xlabel("income per person")
		plt.ylabel("Frequency")

		# This command saves the graph in a pdf file
		figName = 'IncomeDistribution_'+year+'.pdf'
		plt.savefig(figName)
		plt.clf()

	except:
		print "Error! You have given a wrong dataset"