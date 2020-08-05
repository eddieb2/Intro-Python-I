"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


# def calendar_program():
#     month = input('Please enter month: ') or None
#     year = input('Please enter year: ') or None
#
#     current_month = datetime.now().month
#     current_year = datetime.now().year
#
#     if month is None and year is None:
#         # Print the calendar for the current month
#         print("\n")
#         print(calendar.month(current_year, current_month))
#     elif year is None:
#         # Print the calendar for the month input and current year
#         print("\n")
#         print(calendar.month(current_year, int(month)))
#     elif month is not None and year is not None:
#         # Print the calendar for the input month and year
#         print("\n")
#         print(calendar.month(int(year), int(month)))
#
#     sys.exit()
#
#
# calendar_program()

def calendar_program1():
    # declare current month and year
    current_month = datetime.now().month
    current_year = datetime.now().year

    # user_month = None
    # user_year = None

    # if 2 args are entered
    if len(sys.argv) > 2:
        # check if args are digits
        if sys.argv[1].isdigit() and sys.argv[2].isdigit():
            # check that month is 1 - 2 digits
            if 1 <= len(sys.argv[1]) <= 2:
                # check that the value of month is > 0
                if int(sys.argv[1]) > 0:
                    # check that year is 4 digits
                    if len(sys.argv[2]) == 4:
                        # check that year's value is > 0
                        if int(sys.argv[2]) > 0:
                            # save converted args (str >> int)
                            user_month = int(sys.argv[1])
                            user_year = int(sys.argv[2])

                            print(calendar.month(user_year, user_month))
                        else:
                            print('Please enter a valid year!')
                    else:
                        print('Please enter a valid year!')
                else:
                    print('Please enter a valid month!')
            else:
                print('Please enter a valid month!')
        else:
            print('Please enter numbers only!')
    # if 1 arg is entered
    elif len(sys.argv) == 2:
        # check if args are digits
        if sys.argv[1].isdigit():
            # check that month is 1 - 2 digits
            if 1 <= len(sys.argv[1]) <= 2:
                # check that the value of month is > 0
                if int(sys.argv[1]) > 0:
                    user_month = int(sys.argv[1])
                    print(calendar.month(current_year, user_month))
                else:
                    print('Please enter a valid month!')
            else:
                print('Please enter a valid month!')
        else:
            print('Please enter numbers only!')
    # if 0 args are entered
    else:
        print(calendar.month(current_year, current_month))


calendar_program1()
