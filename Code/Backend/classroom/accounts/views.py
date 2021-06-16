from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import StudentForm, FacultyForm, UserRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *
from classes.models import Classroom,Comment,Post

@unauthenticated_user
def FacultyRegistration(request):
    userform = UserRegistration()
    facultyform = FacultyForm()

    if request.method == 'POST':
        userform = UserRegistration(request.POST)
        facultyform = FacultyForm(request.POST, request.FILES)
        if userform.is_valid() and facultyform.is_valid():
            user = userform.save()
            group = Group.objects.get(name ='Faculty')
            user.groups.add(group)          
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

@unauthenticated_user
def StudentRegistration(request):    
    userform = UserRegistration()
    studentform = StudentForm()

    if request.method == 'POST':
        userform = UserRegistration(request.POST)
        studentform = StudentForm(request.POST, request.FILES)
        if userform.is_valid() and studentform.is_valid():
            user = userform.save()
            group = Group.objects.get(name ='Student')
            user.groups.add(group) 
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


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect ('homePage')
        else:
            messages.info (request, 'Email address or Password is incorrect')
            #return render(request, 'sign_in.html')
    context = {}
    return render(request, 'sign_in.html', context)

@login_required(login_url='loginPage')
@student_only
def homePage(request):
    return render (request,'index.html')

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def facultyDashboard(request):
    classroom = Classroom.objects.all()
    class_count=Classroom.objects.count()
    context={
        'classroom' : classroom,'class_count':class_count
    }
    return render(request, 'instructor_dashboard.html',context)