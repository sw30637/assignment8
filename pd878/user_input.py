
import xlrd
import csv
import pandas as pd 
import sys

reload(sys)
sys.setdefaultencoding("utf-8") 
	


def csv_from_excel(xls_file_name, csv_file_name):
	'''Converts xls file to csv'''

	wb = xlrd.open_workbook(xls_file_name)
	sh = wb.sheet_by_name('Data')
	your_csv_file = open(csv_file_name, 'wb')
	wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

	for rownum in xrange(sh.nrows):
		wr.writerow(sh.row_values(rownum))

	your_csv_file.close()



def get_year():
	'''Lets user input an integer between 1800 and 2012 (inclusive) for year.'''
	while True:
		try:
			year = raw_input("Enter year (an integer between 1800 and 2012 (inclusive), or enter 'finish' to exit: ")
			if year == 'finish':
				print "You entered 'finish'. Exiting the interactive mode..."
				return year
			
			elif int(year) >= 1800 and int(year) <=2012:
				return int(year)

        #catches invalid input    
		except ValueError:
			print "\nOops!  Invalid input."
		except KeyboardInterrupt:
			print 'You pressed Ctrl+C! Exiting...'
			sys.exit()   


