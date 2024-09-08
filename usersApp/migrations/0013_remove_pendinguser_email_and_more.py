# Generated by Django 5.1 on 2024-09-07 21:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0012_remove_pendinguser_contact_info'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendinguser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pendinguser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='pendinguser',
            name='password',
        ),
        migrations.AlterField(
            model_name='pendinguser',
            name='first_name',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
