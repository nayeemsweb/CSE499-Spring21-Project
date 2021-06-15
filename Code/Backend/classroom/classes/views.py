from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import ClassroomForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from classes.models import Classroom
from django.contrib.auth.models import User

def createCourse(request):
    classform = ClassroomForm()
    
    if request.method == 'POST':
        classform = ClassroomForm(request.POST, request.FILES)
        if classform.is_valid():
            classform = classform.save(commit=False)
            classform.faculty=request.user
                        
            classform.save()
            return redirect ('facultyDashboard')
    else:    
        context = {'classform':classform}
        return render(request,'create_new_course.html',context)