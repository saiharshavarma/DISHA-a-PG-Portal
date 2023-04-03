from django.shortcuts import render, redirect
from accounts.models import Student, University
from .models import Application
import datetime

# Create your views here.

def profile(request):
    user = request.user
    student = Student.objects.get(user=user)
    if request.method == "POST":
        student.highschool = request.POST['highschool']
        student.cgpa = request.POST['cgpa']
        student.skills = request.POST['skills']
        student.certificates = request.POST['certificates']
        student.transcript = request.FILES.get('transcript')
        student.resume = request.FILES.get('resume')
        student.about_me = request.POST['about_me']
        student.save()
    context = {'student': student}
    return render(request, 'student/profile.html', context)


def home(request):
    user = request.user
    student = Student.objects.get(user=user)
    universities = University.objects.filter(
        deadline__gte=datetime.datetime.now())
    applications = Application.objects.filter(student=student)
    applied_universities = []
    for application in applications:
        applied_universities.append(application.university)
    unapplied_universities = []
    for university in universities:
        if university not in applied_universities:
            unapplied_universities.append(university)
    context = {
        "universities": unapplied_universities,
        "applications": applications,
    }
    return render(request, "student/dashboard.html", context)


def application(request, university):
    student = Student.objects.get(user=request.user)
    university = University.objects.get(university_name=university)
    application = Application.objects.create(
        student=student, university=university, applied_date=datetime.date.today())
    application.save()
    return redirect('student_home')
