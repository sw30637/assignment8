'''
The main module for creating the results for assignment 8. For part (1), the 
program that loads the countries.csv and  income per person data are
located with DataCLass class. The program transforms the data to have 
years as the rows and countries as the columns. For part (3), I chose a histogram 
as my way of displaying the distribution of income per person across all the countries.
For part (4), the function merge_by_year is located in the MergeByYear module. 


Created on Apr 8, 2015
@author: Adam Biesenbach
'''

from GetYear import ReturnUserInput
from CreatePlots import CreateBoxPlotsforRange 
from DataClass import CountryData
import sys

if __name__  =='__main__':
    
    try:
        while True:
           
            """ Get the input from the user. If they return 'finish', print the graphs for 2007-2012.
            If they enter an integer between 1800 and 2015, accept, produce the graphs, and prompt again."""
           
            year = ReturnUserInput()
          
            if year =='finish':
                print "Creating the graphs for 2007-2012."     
                CreateBoxPlotsforRange()
                break       
            else:
                # Just create one instance to use in both functions. 
                DataInstance = CountryData(year)
                DataInstance.CreateBoxPlots()
                DataInstance.CreateHistograms()
                print "Finished running."

    except KeyboardInterrupt:
        print "\n whoops...KeyboardInterrupt... exiting program."
        sys.exit(0)   
            
    except IOError:
        print "\n whoops...I/O error... check to make sure that the file and directory exist for the *.pdf files being created."
        
    print "Finished running."
 
   
            