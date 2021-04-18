from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import StudentForm, FacultyForm, UserRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def FacultyRegistration(request):
    userform = UserRegistration()
    facultyform = FacultyForm()

    if request.method == 'POST':
        userform = UserRegistration(request.POST)
        facultyform = FacultyForm(request.POST)
        if userform.is_valid() and facultyform.is_valid():
            user = userform.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            faculty = facultyform.save(commit=False)
            faculty.user = user
            faculty.save()
            messages.success(request,'Account was created for ' + faculty.user.username)
            return redirect ('loginPage')
    else:
        print (userform.errors, facultyform.errors)

    context = {'facultyform': facultyform, 'userform': userform} 
    return render(request, 'faculty.html', context)


def StudentRegistration(request):
    userform = UserRegistration()
    studentform = StudentForm()

    if request.method == 'POST':
        userform = UserRegistration(request.POST)
        studentform = StudentForm(request.POST)
        if userform.is_valid() and studentform.is_valid():
            user = userform.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            student = studentform.save(commit=False)
            student.user = user
            student.save()
            messages.success(request,'Account was created for ' + student.user.username)
            return redirect ('loginPage')
    else:
        print (userform.errors, studentform.errors)

    context = {'userform': userform, 'studentform': studentform}
    return render(request, 'student.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('emailaddress')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect ('homePage')
        else:
            messages.info (request, 'Email address or Password is incorrect')
            #return render(request, 'sign_in.html')

    return render(request, 'sign_in.html')


def homePage(request):
    return render (request,'index.html' )