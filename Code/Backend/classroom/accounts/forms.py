from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import student, faculty


class StudentForm (forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'      


class FacultyForm(forms.ModelForm):
    class Meta:
        model = faculty
        fields = '__all__' 
        