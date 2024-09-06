from django.shortcuts import redirect, render
from .forms import Nameform, reguser, testform
from django.core.mail import send_mail
from django.contrib import messages
from .models import pendingUser
import datetime, calendar
from django.contrib.auth.models import User
from django.db.models.functions import Now
# from django.forms import formset_factory
# Create your views here.
def get_name(request):
 if request.method == 'POST':
  form = Nameform(request.POST, request.FILES)
  # print(form)
  if form.is_valid():
   fname = form.cleaned_data['first_name']
   lname = form.cleaned_data['last_name']
   email = form.cleaned_data['email']
   pwd = form.cleaned_data['password']
  #  print(pwd)
   regs=pendingUser.objects.create(first_name=fname, last_name=lname, email=email, password=pwd)
  print(pendingUser.objects.filter(first_name=fname)).values()
  #  pends = pendingUser.objects.all()
  #  for i in pends:
  #   print(i.name_time())
  messages.success(request,"conditions are satisfied!!") 
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
   credentials = pendingUser.objects.filter(username = usn, password = pwd)
   print(credentials)
   if credentials.exists():
    now = datetime.datetime.now()
    print(now)
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
   cleaned_essay = essay.cleaned_data['essay']
 return render(request, 'tasking.html', {'form':essay})       