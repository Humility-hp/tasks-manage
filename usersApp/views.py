from django.shortcuts import redirect, render
from .forms import Nameform, reguser, testform
from django.contrib import messages
from .models import daily_task
import datetime
from datetime import datetime, timedelta
import math
# from django.utils import timezone
from django.utils.timezone import make_aware, make_naive
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
# from django.forms import formset_factory
# Create your views here.
def get_name(request):
 if request.method == 'POST':
  form = Nameform(request.POST, request.FILES)
  if form.is_valid():
   fname = form.cleaned_data['first_name']
   lname = form.cleaned_data['last_name']
   email = form.cleaned_data['email']
   pwd = form.cleaned_data['password']
   user=User.objects.create_user(username=fname, last_name=lname, password=pwd, email=email, is_staff=True)
  #  adding a user to a group
  #  Group.objects.get(name='pending-users').user_set.add(user)
   user.save()
   print(f'{fname} is successfully added')
   no_repeat = Group.objects
   groups = ['pending-users','votters','staffs-only']
   for group in groups:
    check = no_repeat.filter(name=group).exists()
    if check and group == 'pending-users':
      no_repeat.get(name=group).user_set.add(user)
    elif not check or group == 'pending-users':
      no_repeat.create(name=group)
      no_repeat.get(name='pending-users').user_set.add(user)
    messages.success(request,f'{user} has been added to pending-users group')
     
  #  user.groups.filter(name='group name').exists(): to know if a user exists in a group
  # my_group = Group.objects.get(name='my_group_name'), my_group.user_set.add(your_user)  
 else:
   form = Nameform()
   messages.error(request, "cross check the credentials carefully")
 return render(request, "pending.html", {'form':form})

def trial(request):
 if request.method == 'POST':
  form = reguser(request.POST, request.FILES)
  if form.is_valid():
   usn = form.cleaned_data['username']
   pwd = form.cleaned_data['password']
   user_login = authenticate(username=usn, password=pwd)
   if user_login is not None:
    login(request, user_login)
    # retrieve date less or equal to certain day
    now = make_aware(datetime.now())
    prev_days = make_aware(datetime.now()-timedelta(days=3))
    search_it = User.objects.filter(Q(date_joined__gte=prev_days) & Q(date_joined__lte=now)).values('username','date_joined')
    print(search_it)
    messages.success(request, f'{request.user} is logged in successfully')
    return render(request, 'tasking.html')
   else:
    print('error message is displayed i.e user does not exist')
    messages.error(request, "invalid credentials")
 else:
  form = reguser()
 return render(request, "task.html", {'form':form})

def userTask(request):
 aware = make_aware(datetime.now())
  # 14th september 2024 at 09:28AM
 naive = make_naive(request.user.date_joined)
 times=[naive,naive+timedelta(days=7)]
 for time in times:
  if time == times[0]:
   starts = time.strftime("%d %B %Y at %I:%M%p")
  else:
   ends = time.strftime("%d %B %Y at %I:%M%p")
  # greetings handler
  time = datetime.now().hour
  if time < 12:
   greetings = "Morning"
  elif time>12 and time<16:
   greetings= "Afternoon"
  else:
   greetings= "Evening"

  # retrieve request.user's essay records
  records = daily_task.objects.filter(created_by=request.user).values('essay').count()
 if request.method == "POST":
  essay = testform(request.POST, request.FILES)
  if essay.is_valid():
   record = daily_task.objects.filter(created_by=request.user).values('essay')
  #  print(record)

   cleaned_essay = essay.cleaned_data['essay']
    # confirm if less than days from the day of registration
   aware = make_aware(datetime.now())
   if aware < request.user.date_joined + timedelta(days=30):
    # if recently added item is 24hrs earlier or exacly
    # prev_time = make_aware(datetime.now()-timedelta(minutes=9))
    # essay_lessthan_24_hr_ago = daily_task.objects.filter(created_by=request.user).filter(Q(created_at__gt=prev_time) & Q(created_at__lte=aware))
    # print(essay_lessthan_24_hr_ago)
    date_recent_item = daily_task.objects.filter(created_by=request.user).order_by('-created_at').values('created_at')[0]['created_at']
    print(date_recent_item+timedelta(days=1))
    if date_recent_item+timedelta(hours=12)<=make_aware(datetime.now()):
     print('yes date is 1day or more ago')
     essay_splitted = cleaned_essay.split()
     sorted_essay = sorted(essay_splitted, key=len, reverse=True)
     if len(sorted_essay[6])>=4:
      daily_task.objects.create(created_by=request.user,essay=cleaned_essay)
      msg = 'Tests passed! essay saved to the database'
     else:
      msg = 'essay must contain atleast six-three letter words'
    else:
      # time restrain here!
      print('time still less than expected')
      essay_untill = date_recent_item + timedelta(days=1)-make_aware(datetime.now())
      print(date_recent_item)
      print(date_recent_item+timedelta(days=1))
      time_split=str(essay_untill).split(":")
      # make_aware(time_remaining)
      # print(time_remaining,hours)
      msg = f' next essay must 2hrs from recent essay wait for{time_split[0]}minutes:{time_split[1]}seconds'
   else:
     msg = 'Your duration of tasks is exceeded'
  else:
   msg = 'Essay is invalid/empty!!'
  # dont forget to attach a message whenever the backend fails 
 return render(request, 'tasking.html', {'form':essay, 'msg':msg, 'starts':starts, 'ends':ends, 'greets':greetings, 'records':records})       