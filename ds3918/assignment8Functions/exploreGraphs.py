# Name: 	exploreGraphs.py
# Author: 	Denis Stukal
# Date: 	April 12, 2015
# Summary:	Defines ExploreGraphs class that stores data for a given year,
# 			makes and saves histograms and boxplots. 
########################################################################################## 

import pandas as p
import matplotlib.pyplot as plt

class ExploreGraphs:
    '''
    An instance has 2 attributes by default: year and dataset. 
    2 functions: 	makeBoxplot() creates a 3rd attribute with a boxplot
    				saveBoxplot() saves the boxplot from self.figure to the current directory
    '''
    def __init__(self, dataset, year):
    	'''
    	Initializes an instance with 2 attributes: year and dataset specified as arguments.
    	'''
        self.year = year
        self.data = dataset

    def makeBoxplot(self):
    	'''
    	Creates a boxplot using self.data (self.year used in the title).
    	NB! The x-axis limits are fixed for all years for the ease of comparison over time. 
    	'''
        newFigure = plt.figure()
        newAx = newFigure.add_subplot(1,1,1)
        self.boxplot = self.data.boxplot(ax = newAx, column = 'Income', by = 'Region')
        # Change x-axis labels
        self.boxplot.set_xticklabels(['Africa','Asia','Europe','North America','Oceania', 'South America'], fontsize = 'small', rotation = 30)
        # Setting the y axis for comparability over time
        self.boxplot.set_ylim(0,70000)
        # Change the title
        self.boxplot.set_title('Income distribution in year %d' %(self.year))
        # No name for the x axis
        self.boxplot.set_xlabel('')
    
    def saveBoxplot(self):
    	'''
    	Saves self.boxplot as a pdf 
    	'''
        plot = self.boxplot.get_figure()
        plot.savefig('boxplot_for_year_%d.pdf' %(self.year))
        
    def makeHistogram(self):
    	'''
    	Creates a histogram using self.data (self.year used in the title)
    	NB! The x-axis limits are *not* fixed over time. Use this graph to look at a snapshot. 
    	'''
    	newFigure = plt.figure()
    	newAx = newFigure.add_subplot(1,1,1)
    	self.histogram = self.data['Income'].hist(ax = newAx, color = 'green')
        self.histogram.set_title('Distribution of income across countries in %s' % self.year)
        self.histogram.set_xlabel('')
    
    def saveHistogram(self):
    	'''
    	Saves self.histogram as a pdf 
    	'''
    	plot = self.histogram.get_figure()
    	plot.savefig('histogram_for_year_%d.pdf' %(self.year))

