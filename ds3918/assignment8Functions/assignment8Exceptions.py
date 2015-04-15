# Name: 	assignment8Exceptions.py
# Author: 	Denis Stukal
# Date: 	April 12, 2015
# Summary:	Defines makeOutput() that merges the data sets, creates a ExploreGraphs object, 
# 			makes a boxplot and saves it. 
########################################################################################## 

class WrongInput(Exception):
    def __str__(self):
        return "Check your input files, input year, and data set."



