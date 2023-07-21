import datetime
# # for current date
# print(datetime.datetime.now())
# # set date
# a = datetime.datetime(1999, 12, 12, 12, 12, 12)
# print("year =", a.year)
# print("month =", a.month)
# print("hour =", a.hour)
# print("minute =", a.minute)
# print("timestamp =", a.timestamp())

# from datetime import date
# # format year, month, date
# my_date = date(1996, 12, 11)
# print("Date passed as argument is", my_date)
# print("Date components", my_date.year, my_date.month, my_date.day)
# # for current date
# today = date.today()
# print("Today's date is", today)
# # Printing date's components
# print("Date components", today.year, today.month, today.day)

# from datetime import time
# my_time = time(13, 24, 56)
# print("Entered time", my_time)
# print("hour =", my_time.hour)
# print("minute =", my_time.minute)
# print("second =", my_time.second)
# print("microsecond =", my_time.microsecond)
# my_time = time(minute = 12)
# print("\nTime with one argument", my_time)
# my_time = time() # 0
# print("\nTime without argument", my_time)

# current
from datetime import datetime

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

from datetime import datetime
date_string = '2009-11-29 03:17 PM'
format ='%Y-%m-%d %H:%M %p'
my_date = datetime.strptime(date_string, format)
# This prints '2009-11-29 03:17 AM'
print (my_date.strftime(format))