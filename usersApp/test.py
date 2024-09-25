import calendar, datetime, time, zoneinfo
from django.utils import timezone
diff = datetime.datetime.now()
if diff.hour <12:
 print('good morning sir')
elif diff.hour >12 and diff.hour < 16:
 print("Good afternoon sir")
else:
 print('good evening')
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.leapdays(2000,2025)): returns numbers of leap year btw this years
# print(calendar.isleap(2004)): tell if the year in bracket is a leap year
# print(calendar.weekday(2024, 8, 15))// return 0- either -6 meaning the day for
# print(calendar.weekheader(3))// print it to know what it signifies
# print(calendar.monthrange(2024, 8))
# print(calendar.monthcalendar(2024, 8))
# print(calendar.month_abbr[12])
# this = datetime.datetime.now()
# day1 = datetime.date(2020,9,22)
# day2 = datetime.date(2020,6,3)
# trying timeone
# this one gives me in nigerian time
# atrial = datetime.datetime.now()
# print(atrial)

# lesson learnt from the this app:
# 1.change time zone i.e go to setting, set TIME_ZONE = 'Africa/lagos'
"""2. time from model is an aware type, from python or datetime.datetime.now() is naive, to convert naive to aware, import 'make_aware(pass the time here)' this way you can perform other calculations regarding time wwith this
3.timedeta helps to reverse certain times backward or forward however needed to use: datetime.datetime.now()-deltatime(days or hour etc = 2)
4. to get user's date of joining, do: request.user.date_joined

"""
# learning to sort words by its length
s= "the quick brown fox jumped over the lazy brown dog's back"
from collections import Counter
wordcount = Counter(s.split())
# print(wordcount.items())
for key,val in sorted(wordcount.items(),key = lambda pair:len(pair[0])):
 print(str(val),key)

# or you can also do it this way
lists = s.split(" ")
sorted_essay = sorted(lists, key=len, reverse=True)
print(len(sorted_essay[3]), sorted_essay[3])
if len(sorted_essay[3])>=4:
 print('the word at the fifth position is upto four letter words')
