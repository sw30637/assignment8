####################################################################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 8
#
#	This file contains the class that will using exploratory data analysis tools to graphically explore the distribution of income per person by region
#	The class takes in the year input given by the user and plots boxplots or histograms and stores them in files
#
####################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from MergeDataFunction import *

# This class will take in the merged data set and do a graphical analysis based on the regions
class DataAnalysis:

	# The constructor function which defines the class variable
	def __init__(self, year):
		self.year = year

	# Function defined to do analysis with boxplots 
	def Plot_BoxPlots(self):

		# Calls the merge function to get the income per year per region
		dataset = merge_by_year(self.year)
		# Give proper commands to plot the boxplot
		dataset.boxplot('Income', by = 'Region', rot = 90)
		plt.title('Boxplot for the income per person by region for the year '+ self.year)
		plt.xlabel('Region')
		plt.ylabel('Income per person')
		plt.ylim(10**2, 10.5**5)
		plt.yscale('log')

		# This command saves the graph in a pdf file
		figName = 'Boxplot_'+self.year+'.pdf'
		plt.savefig(figName)
		plt.clf()

	def Plot_Histogram(self):

		# Calls the merge function to get the income per year per region
		dataset = merge_by_year(self.year)
		dataset = dataset.T
		# Give proper commands to plot the histogram
		plt.hist(dataset.ix['Income'].dropna().values,bins=20)
		plt.title('Histogram for the income per person by region for the year '+ self.year)
		plt.xlabel("Income per person")
		plt.ylabel("Frequency")

		# This command saves the graph in a pdf file
		figName = 'Histogram_'+self.year+'.pdf'
		plt.savefig(figName)
		plt.clf()



