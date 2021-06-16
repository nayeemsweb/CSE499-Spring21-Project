from django import forms
from .models import Classroom,Post,Comment

class ClassroomForm(forms.ModelForm):
    course_description = forms.CharField(widget= forms.Textarea)
    class Meta:
        model=Classroom
        fields = ['course_title','course_subtitle','course_description','class_pics','course_section','class_time']
