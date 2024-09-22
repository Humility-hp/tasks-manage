from django.shortcuts import redirect, render
from .forms import Nameform, reguser, testform
from django.contrib import messages
from .models import daily_task
import datetime
from datetime import datetime, timedelta
# from django.utils import timezone
from django.utils.timezone import get_default_timezone_name, activate, make_aware
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
 if request.method == "POST":
  essay = testform(request.POST, request.FILES)
  if essay.is_valid():
   # make time aware
    aware = make_aware(datetime.now())
    # add item to database and test it
    cleaned_essay = essay.cleaned_data['essay']
  # confirm if less than  days from the day of registration
    if aware < request.user.date_joined + timedelta(days=10):
    # retrieve date less than or equal to 2 hours
     prev_time = make_aware(datetime.now()-timedelta(hours=24))
    #  .filter(Q(date_joined__gte=prev_time) & Q(date_joined=aware))
     essay_lessthan_24_hr_ago = daily_task.objects.filter(created_by=request.user).filter(Q(created_at__gte=prev_time) & Q(created_at__lte=aware))
     if essay_lessthan_24_hr_ago:
        #test if essay is more than 10 three later words first
      essay_splitted = cleaned_essay.split()
      sorted_essay = sorted(essay_splitted, key=len, reverse=True)
      if len(sorted_essay[6]) >=4:
       daily_task.objects.create(created_by=request.user,essay=cleaned_essay)
       print('essay is saved successfully into the database')
    else:
     print("this tasks time limit exceeded")
  
 return render(request, 'tasking.html', {'form':essay})       