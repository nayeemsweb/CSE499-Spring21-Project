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
    # classform=ClassroomForm(request.POST or None)
    if request.method=="POST":
        classforms=Classroom()
        classforms.faculty=request.user
        classforms.course_title=request.POST.get('title')
        classforms.course_subtitle=request.POST.get('subtitle')
        classforms.course_description=request.POST.get('description')
        # classforms.course_pics=request.POST.get('inputGroupFile04')
        classforms.save()
        # classform.save()
        messages.success(request,'successful')
        return redirect ('facultyDashboard')
    # else:
    #     print (classform.errors)
    # context={'classform':classform}
    return render(request,'create_new_course.html')