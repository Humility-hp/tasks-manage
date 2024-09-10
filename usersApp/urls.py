from . import views
from django.urls import path

# urls here below
urlpatterns=[
 path('form', views.get_name, name='form'),
 path('task', views.trial, name='take-task'),
 path('tasking', views.userTask, name='taking-tasking')
]