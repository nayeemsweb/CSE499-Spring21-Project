from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import StudentProfileForm, FacultyProfileForm
# Create your views here.

def student_profile_signup(request):
    return render(request, 'sign_up.html')
        