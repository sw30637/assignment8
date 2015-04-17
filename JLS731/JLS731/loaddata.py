'''
Created by: Joseph Song (JLS731)
Created on: 4/10/2015
Assignment 8
Description: Loads in the csv and xlsx files and returns a DataFrame dataset
'''

import pandas as pd

def loadcsvdata(filename):
    ''' Loads csv file and returns a DataFrame'''
    data = pd.read_csv(filename)
    return data

def loadxlsxdata(filename):
    '''Loads xlsx file and returns a DataFrame'''
    data = pd.read_excel(filename, sheetname = 0, index_col = 0)
    data_transpose = data.transpose()
    data_transpose.columns.name = 'Country'
    return data_transpose


