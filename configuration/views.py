from django.shortcuts import render, redirect
from accounts.models import Student, University


def home(request):
    user = request.user
    student = list(Student.objects.filter(user=user))
    university = University.objects.filter(user=user)
    if student:
        return redirect("student_home")
    else:
        return redirect("university_home")
    

def profile(request):
    user = request.user
    student = list(Student.objects.filter(user=user))
    university = University.objects.filter(user=user)
    if student:
        return redirect("student_profile")
    else:
        return redirect("university_profile")
