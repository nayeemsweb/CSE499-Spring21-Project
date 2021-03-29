from django.shortcuts import render , redirect
from django.contrib import messages

# Create your views here.

def student_profile_view(request):
    if request.method == 'POST':
        