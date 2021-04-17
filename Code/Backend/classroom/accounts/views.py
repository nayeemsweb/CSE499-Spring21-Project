from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import StudentForm, FacultyForm, UserRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def FacultyRegistration(request):
    userform = UserRegistration()
    facultyform = FacultyForm()

    if request.method == 'POST':
        userform = UserRegistration(request.POST)
        facultyform = FacultyForm(request.POST)
        if userform.is_valid() and facultyform.is_valid():
            userform.save()
            facultyform.save()
            user = userform.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect ('login')

    context = {'facultyform': facultyform, 'userform': userform} 
    return render(request, 'faculty.html', context)


def StudentRegistration(request):
    userform = UserRegistration()
    studentform = StudentForm()

    if request.method == 'POST':
        userform = UserRegistration(request.POST)
        studentform = StudentForm(request.POST)
        if userform.is_valid() and studentform.is_valid():
            userform.save()
            studentform.save()
            user = userform.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect ('login')

    context = {'userform': userform, 'studentform': studentform}
    return render(request, 'student.html', context)

def login(request):
    return render(request, 'sign_in.html')