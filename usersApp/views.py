from django.shortcuts import redirect, render
from .forms import Nameform, reguser, testform
from django.core.mail import send_mail
from django.contrib import messages
from .models import daily_task
import datetime, calendar
from datetime import datetime, timezone
# from django.utils import timezone
from django.utils.timezone import get_default_timezone_name, activate, make_aware, is_aware
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
    # know the database timezone
    # print(request.user.date_joinecd d) a users date_joined
    print(activate('Africa/Lagos'))
    aware = make_aware(datetime.datetime.now())
    print(is_aware(aware))
    print(datetime.datetime(1997,9,26,14,12,20, tzinfo=timezone.ZoneInfo("Africa/Lagos")))
    time_difference=aware-request.user.date_joined 
    print(time_difference.total_seconds()/(60*60))
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
   cleaned_essays = essay.cleaned_data['essay']
  # use exists on objects to validate the presence of a query
   
  #  check same users items in daily_task
  
 return render(request, 'tasking.html', {'form':essay})       