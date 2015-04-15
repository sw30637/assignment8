import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
class analysisclass():
	"""this is a class that uses exploratory data analysis tools"""
	def __init__(self,analysisDF,year):
		self.analysisDF = analysisDF
		self.year = year
	def __str__(self):
		print "Dataframe is", self.analysisDF, '\n',"Year for analysis is:",self.year

	def drawboxplot(self):
		""" This is the method to generate boxplot for merged dataframe
		according to different region"""
		DF = self.analysisDF
		year = self.year
		DF.boxplot('Income',by = ['Region'],rot = 90)
		plt.title('Year:'+ str(year))
		plt.ylabel('Income per person')
		plt.xlabel('Region')
		plt.ylim(10**2,10.5 **5)
		plt.yscale('log')
		plt.show(block = False)
		return None

