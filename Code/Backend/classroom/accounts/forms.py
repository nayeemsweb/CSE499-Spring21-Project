from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models import fields
from .models import Student, Faculty, User


class StudentForm (forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentID', 'department']      
    #    exclude = ['user']

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['facultyID', 'bio', 'department']

class UserRegistration(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
        