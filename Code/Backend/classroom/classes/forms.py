from django import forms
from django.forms.widgets import Textarea
from .models import Classroom,Post,Comment

class ClassroomForm(forms.ModelForm):
    course_description = forms.CharField(widget= forms.Textarea)
    class Meta:
        model=Classroom
        fields = ['course_title','course_subtitle','course_description','class_pics','course_section','class_time','class_code']


class PostForm(forms.ModelForm):
    post= forms.CharField(widget=Textarea)
    class Meta:
        model= Post
        fields = ['post']
