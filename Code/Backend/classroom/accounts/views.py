from django.shortcuts import render , redirect
from django.contrib import messages

# Create your views here.

def student_profile_signup(request):
    if request.method == 'POST':
        