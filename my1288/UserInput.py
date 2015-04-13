##############################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 8
#
#	This file contains the function that takes the correct input from the user
#	The function will keep taking input from the user until the user types in 'finish'
#
##############################################################

def TakeUserInput():

	# Set a boolean variable to keep track of the while loop
	check = True

	# Run a while loop to keep on taking inputs from the user until finish is entered
	while (check == True):

		# use the try/except statements to check whether the user gives the correct input
		try:
			input_year = raw_input("Please Enter the year between 1800 and 2012 for which you view the income. Type 'Finish' to continue.")

			# Check whether the input is actually a year. This sets x to True so that further tests can be applied
			try:
				int(input_year)
				x = True

			# exit the function if finish is typed in or raise an error for a wrong format
			except:
				if (input_year.capitalize() == 'Finish'):
					check = False
					return 'Finish'
				else:
					print "You have typed in the year in wrong format. Please use the 4 digit format eg 2012"
					x = False

		# Exits the program if there is a keyboard interrupt
		except (KeyboardInterrupt, SystemExit):
			raise

		# Check for the other errors possible
		if (x==True):
			if len(input_year) != 4:
				print "You have typed in the year in wrong format. Please use the 4 digit format eg 2012"
			elif (int(input_year)<1800) or (int(input_year)>2012):
				print "These years do not exist in the Database. Try again."
			else:
				return input_year
		else:
			pass

