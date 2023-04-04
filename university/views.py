from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import University, Student
from student.models import Application
# Create your views here.

@login_required(login_url='login')
def profile(request):
    user = request.user
    university = University.objects.get(user=user)
    if request.method == "POST":
        university.phone = request.POST['phone']
        university.user.email = request.POST['email']
        university.deadline = request.POST['deadline']
        university.address = request.POST['address']
        university.url = request.POST['url']
        university.save()
    context = {'university': university}
    return render(request, 'university/profile.html', context)


@login_required(login_url='login')
def home(request):
    user = request.user
    university = University.objects.get(user=user)
    applications = Application.objects.filter(university=university)
    context = {
        "applications": applications,
    }
    return render(request, "university/dashboard.html", context)


@login_required(login_url='login')
def changeStatus(request, application):
    application = Application.objects.get(id=application)
    status = request.POST.get('status-'+str(application.id))
    application.status = status
    application.save()
    return redirect('university_home')
