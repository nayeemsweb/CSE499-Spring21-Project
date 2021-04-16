from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import StudentForm, FacultyForm
from django.contrib.auth.forms import UserCreationForm


def facultyRegistration(request):
    form = FacultyForm()
    context = {'form': form}

    return render(request, 'sign_up.html', context)