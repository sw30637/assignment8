##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 8
#
#	This file contains the function merge_by_year(year)
#	The function will read in the data sets and then create a new data set which will have three columns titled Country, Region, Income
#
##############################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def merge_by_year(year):

	# Read in the available datasets
	countries = pd.read_csv('countries.csv')
	income = pd.read_csv('indicatorgapmindergdp_per_capita_ppp.csv')

	# This will create a temporary dataframe that is to be merged with the countries dataframe
	new = pd.DataFrame({"Country":income['gdp pc test'],"Income":income[year]})
	merged_data = pd.merge(countries, new, on='Country',how='inner')

	return merged_data
