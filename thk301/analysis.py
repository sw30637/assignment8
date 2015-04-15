# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  analysis.py 
#  April 9,2015
#
#  analysis.py
#  Displays graphs when a dataframe (which will be grouped by Region) and a year is given
#
###################################
import matplotlib.pyplot as plt

class analysisClass():
    
  def __init__(self, thisDF, year): 
    '''
    thisDF is a pandas dataframe that merges data from countries.csv and indicator gapminder gdp_per_capita_ppp.xlsx 
    for a given year
    ''' 
    self.thisDF = thisDF
    self.year = year
       
       
  def analysisFunction(self):
    '''
    Plot histogram, boxplot, and pie
    '''
    groupedDF = self.thisDF.groupby(self.thisDF['Region'])   #group by Region.   5 Regions will be grouped
    for name, group in groupedDF:
        fig = plt.figure(figsize=(14,8), dpi=90)
        ax1 = plt.subplot(131)    #first one
        ax2 = plt.subplot(132)    #second one
        ax3 = plt.subplot(133)    #third one
       
        ######   first plot ######
        group['Income'].hist(bins=10, ax=ax1, alpha=0.5)
        ax1.set_ylabel('Frequency')
        ax1.set_xlabel('Income (GDP per Capita)')
        ax1.grid(False)
        ax1.tick_params(axis='x',  labelsize=7)
        
        ######   second plot ######
        group.boxplot(ax=ax2)
        ax2.set_ylabel('Income (GDP per Capita)')
        thisTitle ="%d - %s"%(self.year, name)
        ax2.set_xlabel(thisTitle)
        ax2.grid(False)
        
        ######   third plot ######
        group.plot(kind='pie',  labels=group['Country'], subplots=True, ax=ax3, fontsize='5')
        ax3.legend().set_visible(False)
        ax3.axis('equal')
        
        plt.subplots_adjust(bottom=.2, wspace = 0.2, left=.1, right=.6)    
        fig.set_tight_layout(True)
        plt.savefig('%d - %s.png' %(self.year, name))       #save 2007-NORTH AMERICA.png
        
    return None
    
