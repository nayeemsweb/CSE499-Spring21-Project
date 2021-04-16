from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import StudentForm, FacultyForm, UserRegistration
from django.contrib.auth.forms import UserCreationForm


def facultyRegistration(request):
    form = FacultyForm()
    context = {'form': form}

    return render(request, 'sign_up.html', context)


def StudentRegistration(request):
    userform = UserRegistration()
    studentform = StudentForm()

    context = {'userform': userform, 'studentform': studentform}

    return render(request, 'sign_up.html', context)