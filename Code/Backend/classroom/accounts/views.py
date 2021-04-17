from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import StudentForm, FacultyForm, UserRegistration
from django.contrib.auth.forms import UserCreationForm


def FacultyRegistration(request):
    userform = UserRegistration()
    facultyform = FacultyForm()
    context = {'facultyform': facultyform, 'userform': userform} 
    return render(request, 'faculty.html', context)


def StudentRegistration(request):
    userform = UserRegistration()
    studentform = StudentForm()

    context = {'userform': userform, 'studentform': studentform}

    return render(request, 'student.html', context)