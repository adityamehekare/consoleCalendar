from __future__ import print_function
from datetime import datetime
import sys
import pytz

months_dict = {1:'January',2: 'February',3:'March',4:'April',5: 'May',6: 'June',
 			  7:'July', 8:'August',9:'September',10: 'October', 11:'November',12: 'December'}
no_of_days = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
days_of_week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']



def check_leap_year(year):
	'''



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

	'''

	dtime = datetime.now(pytz.timezone('Asia/Kolkata'))
	date = dtime.day
	month = dtime.month
	year = dtime.year	

	return date, month, year


def print_calendar(year,month,date):
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



def main():
	try:
		date, month, year = get_current_date()
	except:
		print("Can not fetch current date and time")

	
	try:
		check_leap_year(year)

		print_calendar(year,month,date)

	except:
		print("Error in priting calendar")


#calling main function
if __name__ == '__main__':
   
    main()

