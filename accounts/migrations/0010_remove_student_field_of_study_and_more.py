# Generated by Django 4.1.7 on 2023-04-03 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_university_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='field_of_study',
        ),
        migrations.AlterField(
            model_name='university',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 23, 30, 14, 683525)),
        ),
    ]
