from django import forms
from .models import Classroom,Post,Comment

class ClassroomForm(forms.ModelForm):
    class Meta:
        model=Classroom
        fields=['']