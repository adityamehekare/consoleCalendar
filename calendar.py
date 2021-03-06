from __future__ import print_function
from datetime import datetime
import pytz
import argparse

months_dict = {1:'January',2: 'February',3:'March',4:'April',5: 'May',6: 'June',
 			  7:'July', 8:'August',9:'September',10: 'October', 11:'November',12: 'December'}
no_of_days = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
days_of_week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']


class bcolors:
	class fg: 
		black='\033[30m'
		red='\033[31m'
		green='\033[32m'
		orange='\033[33m'
		blue='\033[34m'
	
	class bg: 
		black='\033[40m'
		red='\033[41m'
		green='\033[42m'
		orange='\033[43m'
		violet= '\033[46m'

	RED     = '\033[91m'
	GREEN   = '\033[92m'
	BLUE    = '\033[94m'
	CYAN    = '\033[96m'
	WHITE   = '\033[97m'
	YELLOW  = '\033[93m'
	MAGENTA = '\033[95m'
	GREY    = '\033[90m'
	BLACK   = '\033[90m'
	DEFAULT = '\033[99m'
	BOLD    = '\033[1m'
	UNDERLINE = '\033[4m'
	END     = '\033[0m'








def check_leap_year(year):
	'''
	It checks the leap year conditions on the given year
	and update the no_of_days global dict to add the corresponding days for
	the month of February.

	Args : 

		year (integer) - the value of year to be test as leap year

	Return :
		None


	'''

	if (year%400 == 0):
		no_of_days[2]=29
	elif (year%100 == 0):
		no_of_days[2]=28
	elif (year%4 == 0):
		no_of_days[2]=29
	else:
		no_of_days[2]=28 


def get_current_date():
	'''
	It is used to fetch the current datetime of specified zone.
	Args:
		None

	Return :
		date (integer) - returns the current date of specified zone.
		month (integer)- returns month number of current date.
		year (integer) - returns the value of current year.

	'''

	dtime = datetime.now(pytz.timezone('Asia/Kolkata'))
	date = dtime.day
	month = dtime.month
	year = dtime.year	

	return date, month, year


def print_calendar(year,month,date):
	"""
	Function used to print the calendar for a given date.

	Args:
		year (integer) - the value of year for which calendar has to be printed.
		month (integer) - the value of month for which calendar has to be printed.
		date (integer) - the value of date to highlight the current date.
	
	Returns:
		None
	"""
	start_pos = datetime(year,month,1).isoweekday()
	start_pos%=7
	start_space = start_pos%7
	st = bcolors.CYAN+bcolors.BOLD+months_dict[month] +" "+str(year)+bcolors.END
	print('{:^30}'.format(st))
	#print('{0} {1}'.format(months_dict[month],year).center(20, ' '))
	#print()	        
	print(''.join(['{0:<3}'.format(bcolors.BLUE+w+bcolors.END+" ") for w in days_of_week]))

	print('{0:<3}'.format('')*start_space, end="")
	for day in range(1,no_of_days[month]+1):
	        # Print day
	        if(day==date):
	        	print('{0:<3}'.format(bcolors.bg.violet+bcolors.BOLD+str(day)+bcolors.END),end=" ")
	        	
	        else:
	        	print('{0:<3}'.format(day),end="")
	        
	        start_pos += 1
	        if start_pos == 7:
	            # If start_pos == 7 (Sunday) start new line
	            print()
	            start_pos = 0 # Reset counter


	print()


def get_changed_month(change_month,current_month,current_year):

	"""
	Function gives the latest year and month from the command line arg change.

	Args:
		change_month (integer) - the amount by which a past/future month is printed.
		current_month (integer)- the value of current month of specified time zone.
		current_year (integer) - the values of current year of specified time zone.

	Returns :
		latest_month (integer) - returns latest value of month after change.
		latest_year (integer)  - returns latest value of year after change.
	"""

	latest_month = change_month+current_month

	if ( latest_month==0):
		return 12, current_year-1
	elif (latest_month<0):
		return latest_month%12,current_year-1
	elif (latest_month<=12):
		return latest_month, current_year
	elif(latest_month==24):
		return 12, current_year+1
	else:
		return latest_month%12,current_year+1




def main(change_month=0):

	#fetching current datetime API using specified time zone
	try:
		date, month, year = get_current_date()
	except:
		print("Can not fetch current date and time")


	#for non-zero argument
	if change_month !=0:
		#Validating the argument
		change_month = int(float(change_month))
		if change_month>12 or change_month< -12:
			raise Exception(bcolors.RED+"Invalide argument! Please check the range for arg."+bcolors.END)

		month, year = get_changed_month(change_month,month,year)
	



	#checking for leap year and printing the calendar
	try:
		check_leap_year(year)

		print_calendar(year,month,date)

	except:
		print("Error in priting calendar")


#calling main function
if __name__ == '__main__':


	parser = argparse.ArgumentParser(description="""This application computes a future calendar
													(future month, for current date) or a past calendar (past month) of 
													a given date. ( provided given date is present 
													in that future/past month) """)
	parser.add_argument('-m','--month', help='''a positive/negative/zero integer, it lies between -12 to 12 to fetch the past or 
												future month of a current date.''', required=False)
	args = vars(parser.parse_args())

	if args['month'] == None :
		print(bcolors.RED+"No command line argument specified. Search for --help."+bcolors.END)
		try:
			main()
		except Exception as e:
			print(e)
	else:
		try:
			main(args['month'])

		except Exception as e:
			print(e)