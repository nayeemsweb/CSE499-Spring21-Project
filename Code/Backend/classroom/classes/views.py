from django.shortcuts import render

# Create your views here.
def createCourse(request):
    return render(request,'create_new_course.html')