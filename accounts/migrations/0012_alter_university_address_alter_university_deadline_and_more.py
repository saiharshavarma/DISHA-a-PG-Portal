# Generated by Django 4.1.7 on 2023-04-03 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_student_about_me_alter_student_certificates_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='address',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 23, 33, 55, 131434)),
        ),
        migrations.AlterField(
            model_name='university',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
