# Generated by Django 5.1 on 2024-09-04 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0009_delete_assign'),
    ]

    operations = [
        migrations.CreateModel(
            name='daily_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('essay', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersApp.pendinguser')),
            ],
        ),
    ]
