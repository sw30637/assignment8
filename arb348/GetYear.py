'''
A module for getting the users year input, and validating that it's correct.

Created on Apr 10, 2015
@author: Adam Biesenbach
'''

import sys

def ReturnUserInput():
    """ A master function that returns the users year input."""

    return (ValidateYear())

def ValidateYear():
    """ Validate that the year the user entered was correct."""
    while True:
        
        # Get the user input. 
        year= GetYear()      
          
        # If the user did not enter anything, prompt again. Else, go on. 
        if year !="":
            # If they entered finish, break out of the while loop. 
            if year=='finish':
                break
            else:
                # If these give the correct year (in the right range and an integer, break the loop. 
                try:
                    if (int(year)<= 2015 and int(year)>=1800) is False or float(year).is_integer() is False:
                        print "Invalid Year."
                        continue
                    else:
                        break
                except ValueError:
                    print "Invalid Year."
                    continue
        else:
            print "Invalid year."   
            continue
    return year

def GetYear():
    """Return the raw input from the user containing the year they want to consider."""
    try:
        year =  raw_input("Year between 1800 and 2012 (or enter 'finish' to exit)? ")
    except KeyboardInterrupt:
        print "\n whoops... KeyboardInterrupt... exiting program."
        sys.exit(0)
    else: 
        return year 

