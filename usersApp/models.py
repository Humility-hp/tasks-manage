from django.db import models
# from django.contrib.auth.models import user
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
from django.contrib import messages
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User, Group


# Create your models here. 
def identity(person):
  return person
def contactVal(contact):
 validate = re.findall("^080.{8}$|^081.{8}$|^090.{8}$|^070.{8}$", contact)
 if not validate:
  raise ValidationError(("%(contact)s must be a nigerian number"), params={"contact":contact})
  
  

class daily_task(models.Model):
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  essay = models.TextField()

  def __str__(self):
    return str(self.created_by)                           