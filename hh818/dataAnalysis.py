'''
Created on Apr 14, 2015

@author: ds-ga-1007
'''
import matplotlib.pyplot as plt

class dataAnalysis():
    def __init__(self, year, df):
        self.year = year
        self.df = df
        
    def plotBox(self):
        '''plot boxplot of income per person by region in a given year'''
        self.df.boxplot('Income', by = 'Region', rot = 20)
        plt.ylim(0, 120000)
        plt.title('Income per Person by region for year ' + self.year)
        plt.xlabel('Region')
        plt.ylabel('Income Per Person')
        
        
        fileName = self.year + 'Box.pdf'
        plt.savefig(fileName)
        plt.clf()

        
        