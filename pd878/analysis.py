

import pandas as pd 
import matplotlib.pyplot as plt 


def plot_year(df):
	"""Plots a histogram of a year's data"""
	plt.figure()
	
	hist = df['Income'].hist(bins = 10)
	hist.set_xlabel("Per Capital Income")
	hist.set_ylabel("Count")

	plt.show()
	plt.close()


class Graph:

	def __init__(self, dataframe, year):
		self.dataframe = dataframe
		self.year = year

	def plot_histogram(self):
		fig = plt.figure()
		
		hist = self.dataframe['Income'].hist(bins = 10)
		hist.set_xlabel("Per Capital Income")
		hist.set_ylabel("Count")

		plt.savefig('Histogram of %s.png' %self.year) 

	def plot_boxplot(self):
		fig = plt.figure()

		box = self.dataframe.boxplot(column = 'Income', by = 'Region')
		box.set_ylabel('Per Capita Income')

		plt.savefig('Boxplot of %s.png' %self.year) 

