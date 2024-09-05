from django.contrib import admin
from .models import pendingUser, daily_task
# Register your models here.
admin.site.register(pendingUser)
admin.site.register(daily_task)