from django.shortcuts import render , redirect
from .models import User, StudentProfile, FacultyProfile
from .forms import StudentProfileForm, FacultyProfileForm
from django.views.generic import CreateView
from django.http import HttpResponse
# Create your views here.

def register(request):
    return render(request, 'sign_up.html')
        

class studentRegister(CreateView):
    model = User
    form_class = StudentProfileForm
    template_name = '../templates/sign_up.html'

class facultyRegister(CreateView):
    model = User
    form_class = FacultyProfileForm
    template_name = '../templates/sign_up.html'

def live(request):
     return render(request,'../templates/live_streams.html') 
