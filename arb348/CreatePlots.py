'''
The module that houses plotting function to plot the whole range
of years from 2007-2012.

Created on Apr 10, 2015
@author: Adam Biesenbach
'''

import numpy as np 
from DataClass import CountryData
    
def CreateBoxPlotsforRange():
    """Runs the CreateBoxPlots functions for a range of dates, generating a set of pdf files
    containing boxplots and histograms."""
    years = np.arange(2007, 2013, 1)
    for eachyear in years:
        DataInstance = CountryData(eachyear)
        DataInstance.CreateBoxPlots()
        DataInstance.CreateHistograms()
        