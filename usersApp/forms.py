from django import forms
from django.forms import ModelForm
from .models import pendingUser
# declare the django class beneath here
class Nameform(forms.Form):
 first_name = forms.CharField(required=True, max_length=20)
 last_name = forms.CharField(required=True, max_length=20)
 email = forms.EmailField(required=True)
 contact_info = forms.CharField(required=True)
 password = forms.CharField(required=True)

 # to style your forms use or visit "django-widget-tweaks"

class reguser(forms.Form):
 username = forms.CharField(required=True, max_length=20)
 password = forms.CharField(required=True, max_length=20)

class testform(forms.Form):
 essay = forms.CharField(widget=forms.Textarea)