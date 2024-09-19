import calendar, datetime, time, zoneinfo
from django.utils import timezone
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.leapdays(2000,2025)): returns numbers of leap year btw this years
# print(calendar.isleap(2004)): tell if the year in bracket is a leap year
# print(calendar.weekday(2024, 8, 15))// return 0- either -6 meaning the day for
# print(calendar.weekheader(3))// print it to know what it signifies
print(calendar.monthrange(2024, 8))
print(calendar.monthcalendar(2024, 8))
print(calendar.month_abbr[12])
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
# codes for another commit
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
# from base.models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class CustomLoginView(LoginView):
 template_name = 'base/login.html'
 fields = '__all__'
 redirect_authenticated_user = True

 def get_success_url(self):
  return reverse_lazy('tasks')

class RegisterPage(FormView):
 template_name = 'base/register.html'
 form_class = UserCreationForm
 redirect_authenticated_user = True 
 success_url = reverse_lazy('tasks')

 def form_valid(self, form):
  user = form.save()
  if user is not None:
   login(self.request, user)
  return super(RegisterPage, self).form_valid(form)
  
 def get(self, *args, **kwargs):
  if self.request.user.is_authenticated:
   return redirect('tasks') 
  return super(RegisterPage, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
 # model = Task
 # changing/reconfigring the templates name
 context_object_name = 'tasks'

 # to make users only get their own data
 def get_context_data(self, **kwargs):
  context =super().get_context_data(**kwargs)
  context['tasks'] = context['tasks'].filter(user=self.request.user)
  context['count'] = context['tasks'].filter(complete=False).count()
  
  search_input = self.request.GET.get('search-area') or ''
  if search_input:
   context['tasks'] = context['tasks'].filter(title__startswith=search_input)

   context['search_input'] = search_input
  return context

class TaskDetail(LoginRequiredMixin, DetailView):
 # model = Task
 context_object_name ='task'
 template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
 # model = Task
 fields = ['title','description','complete']
 success_url = reverse_lazy('task')

 def form_valid(self, form):
  form.instance.user = self.request.user
  print(super(TaskCreate, self).form_valid(form))
  return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
 # model = Task
 fields = '__all__'
 success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
 # model = Task
 context_object_name = 'task'
 success_url = reverse_lazy('tasks')