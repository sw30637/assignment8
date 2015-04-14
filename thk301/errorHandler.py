# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  errorHandler.py 
#  April 10,2015
#
#  Handles various errors from inputs of assignment8.py
#
###################################


import sys


class errorHandlerClass():
    
  def __init__(self, thisError):  
       self.thisError = thisError
      
  def errorHandlerFunction(self):
    '''
    Checks various errors.   Error will terminate the program.  
    '''
    if self.thisError ==  IndexError:  #in case of IndexError
        print "*"*30
        print "You are too advance. Index is out of range."
        print "*"*30
        sys.exit(1)

    elif self.thisError ==  ValueError:  #in case of ValueError
        print "*"*30
        print "You are too advance. Please type in valid value next time"
        print "*"*30
        sys.exit(1)
        
    elif self.thisError ==  NameError:  #in case of NameError
        print "*"*30
        print "You are too advance. Please type in a year"
        print "*"*30
        sys.exit(1)

    elif self.thisError ==  KeyboardInterrupt:   #in case of CTRL + C
        print "*"*30
        print "Keyboard interrupted"
        print "*"*30
        sys.exit(1)
    
    elif self.thisError ==  SyntaxError:   #without an input
        print "*"*30
        print "Please type in a year next time"
        print "*"*30
        sys.exit(1)
        
    elif self.thisError ==  "outRange":    #out of 1800-2012
        print "*"*30
        print "You put in an invalid year. Please type in a year between 1800 to 2012"
        print "*"*30
        sys.exit(1)
        
    elif self.thisError == SystemExit:
        sys.exit(1)
        
    else:
        print "Undefined Error  ----> ", self.thisError    
 