from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import StudentProfile, FacultyProfile, User
class StudentProfileForm(UserCreationForm):
    studentID = forms.CharField(required=True)
    class Meta:
        model= User
        fields= ['first_name','last_name','studentID', 'department', 'email']
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        student = StudentProfile.objects.create(user = user)
        student.studentID = self.cleaned_data.get('studentID')
        student.save()
        return user
        
class FacultyProfileForm(forms.ModelForm):
    facultyID = forms.CharField(required=True)
    bio = forms.CharField(required= True, widget=forms.Textarea)
    class Meta:
        model= User
        fields= ['first_name','last_name','department', 'facultyID', 'bio', 'email']
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        faculty = FacultyProfile.objects.create(user = user)
        faculty.facultyID = self.cleaned_data.get('facultyID')
        faculty.bio = self.cleaned_data.get('bio')
        faculty.save()
        return user
        