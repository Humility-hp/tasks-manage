import calendar, datetime
from django.utils import timezone
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.leapdays(2000,2025)): returns numbers of leap year btw this years
# print(calendar.isleap(2004)): tell if the year in bracket is a leap year
# print(calendar.weekday(2024, 8, 15))// return 0- either -6 meaning the day for
# print(calendar.weekheader(3))// print it to know what it signifies
# print(calendar.monthrange(2024, 8))
# print(calendar.monthcalendar(2024, 8))
# print(calendar.month_abbr[12])
this = datetime.datetime.now()
day1 = datetime.date(2020,9,22)
day2 = datetime.date(2020,6,3)
print(day1-day2)
print(day1 + day2)
if str(day1 - day2) == '111 days, 0:00:00':
 print('yes it is')
 # day2 = day2 + datetime.date.today()
 print(day2)
else:
 print('no it isnt')

