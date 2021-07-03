from django import forms
from django.forms.widgets import Textarea
from .models import Classroom,Post
from ckeditor_uploader.fields import RichTextUploadingField
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