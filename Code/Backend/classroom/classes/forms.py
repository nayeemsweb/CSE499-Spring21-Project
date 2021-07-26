
from django import forms
from django.forms.widgets import DateTimeInput, Textarea,TextInput
from django.forms import DateTimeField
from .models import Classroom,Post,exam ,student_submission
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.admin.widgets import AdminSplitDateTime
class ClassroomForm(forms.ModelForm):
    course_description = forms.CharField(widget= forms.Textarea)
    class Meta:
        model=Classroom
        fields = ['course_title','course_subtitle','course_description','class_pics','course_section','class_time','class_code']


class PostForm(forms.ModelForm):
    # post= forms.CharField(widget=forms.Textarea,label="")
    # post=RichTextUploadingField(blank=True,null=True)

    # email = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model= Post
        fields = ['post']
        # widgets = { 'post': forms.Textarea(attrs={'cols': 200,'rows':50})}
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['post'].label = ""
        self.fields['post'].widget.attrs['cols'] = 100
        self.fields['post'].widget.attrs['rows'] = 2
        self.fields['post'].widget.attrs['padding-left'] = 150

class ExamForm(forms.ModelForm):
    # exam_time = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )

    exam_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    class Meta:
        model = exam         
        fields = ['exam_title','exam_post','exam_time','total_marks']
        
   