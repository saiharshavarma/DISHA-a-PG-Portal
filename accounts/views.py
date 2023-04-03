from django.db import reset_queries
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Student, University
from django.contrib import messages


def registerStudent(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register_student')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('register_student')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                student = Student.objects.create(user=user, phone=phone)
                student.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('register_student')
    else:
        return render(request, 'accounts/register_student.html')


def registerUniversity(request):
    if request.method == 'POST':
        university_name = request.POST['university_name']
        address = request.POST['address']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register_university')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('register_university')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                university = University.objects.create(
                    user=user, university_name=university_name, address=address, phone=phone)
                university.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('register_university')
    else:
        return render(request, 'accounts/register_university.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
