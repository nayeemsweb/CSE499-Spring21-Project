from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile, FacultyProfile

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('first_name', 'last_name,' 'email')


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('studentID', 'Department')

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model= FacultyProfile
        fields = ('faculty_id', 'Department', 'bio')