from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from .forms import ClassroomForm
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from classes.models import Classroom, student_classroom
from django.contrib.auth.models import User
from accounts.models import Student,Faculty

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

def courseDetail(request,pk):
    course_detail = Classroom.objects.get(class_codes = pk)
    context ={'course_detail':course_detail}
    return render(request,'course_detail_view.html',context)

def courseDelete(request,pk):
    course = get_object_or_404(Classroom, class_codes=pk)
    if course.faculty != request.user:
        raise Http404()
    course.delete()
    return redirect('facultyDashboard')

def courseEdit(request,pk):
    PreviousCourse = Classroom.objects.get(class_codes=pk)
    courseForm= ClassroomForm(instance=PreviousCourse)

    if request.method == 'POST':
        courseForm = ClassroomForm(request.POST, instance=PreviousCourse)
        if courseForm.is_valid():                        
            courseForm.save()
            return redirect ('/')

    
    context = {'courseForm':courseForm}

    return render(request,'course_edit_view.html',context)

def joinclass(request):

    if request.method == 'POST':
        #print(request.POST['class_code'],"===============")
        joining_code=request.POST['class_code']
        course = Classroom.objects.filter(class_code=joining_code).first()
        NewStudent = Student.objects.filter(user=request.user).first()
        if course:
            student_classroom.objects.get_or_create(student=NewStudent, classroom=course)
        return redirect ('homePage')
    else:
        return render(request,'join_class.html')