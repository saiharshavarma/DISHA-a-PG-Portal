from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(blank=True, unique=True, null=True)
    photo = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    about_me = models.TextField(null=True, default="", blank=True)
    skills = models.TextField(null=True, default="", blank=True)
    certificates = models.TextField(null=True, default="", blank=True)
    highschool = models.DecimalField(decimal_places=1, max_digits=3, null=True, blank=True)
    cgpa = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    transcript = models.FileField(null=True, blank=True)
    resume = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(f'{self.user.first_name}' + ' ' + f'{self.user.last_name}')


class University(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=100, null=True, unique=True)
    address = models.TextField(default="", blank=True, null=True)
    phone = PhoneNumberField(blank=True, unique=True, null=True)
    deadline = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(f'{self.university_name}')
