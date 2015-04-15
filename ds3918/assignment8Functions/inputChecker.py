# Name: 	inputChecker.py
# Author: 	Denis Stukal
# Date: 	April 12, 2015
# Summary:	Defines 2 function to check user's input: isInputNumeric() and isInputRightInterval()			 
########################################################################################## 


def isInputNumeric(someInput):
    '''
    Takes an input and returns True if the input can be made integer, False otherwise. 
    '''
    try: 
        someInput = int(someInput)
        return True
    except:
        return False


def isInputRightInterval(someInteger):
    '''
    Takes an integer and returns True if it's between 1800 and 2012, False otherwise.
    '''
    if someInteger >= 1800 and someInteger <= 2012:
        return True
    else:
        return False


