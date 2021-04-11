from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from .models import User, StudentProfile, FacultyProfile
from .forms import StudentProfileForm, FacultyProfileForm
from django.views.generic import CreateView
# Create your views here.
class signIn(CreateView):
    template_name = '../templates/sign_in.html'
        

class studentRegister(CreateView):
    model = User
    form_class = StudentProfileForm
    template_name = '../templates/sign_up.html'
    success_url = reverse_lazy('studentRegister')
    

class facultyRegister(CreateView):
    model = User
    form_class = FacultyProfileForm
    template_name = '../templates/sign_up.html'