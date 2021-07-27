from django import db
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState
from django.db.models.fields import DateField
from accounts.models import Faculty,Student
from django.urls import reverse
import uuid
import random
import string
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class ClassTime (models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Classroom (models.Model):
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    # facultyiD=models.OneToOneField(Faculty, on_delete= models.CASCADE)
    class_codes=models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    class_pics=models.ImageField(null=True, blank=True)
    course_title=models.CharField(max_length=20)
    course_subtitle=models.CharField(max_length=20,null=True)
    course_description=models.CharField(max_length=500,null=True)
    course_section = models.CharField(max_length=3,null=True)
    class_code = models.CharField(max_length=6, null=True, blank=True, unique=True)
    class_time = models.ForeignKey(ClassTime,null=True,on_delete= models.SET_NULL)

    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self):
        if not self.class_codes:
            # Generate ID once, then check the db. If exists, keep trying.
            self.class_codes = self.id_generator()
            while Classroom.objects.filter(urlhash=self.class_codes).exists():
                self.class_codes = self.id_generator()
        super(Classroom, self).save()
    
    def __str__(self) -> str:
        return self.course_title + ' Section ' +self.course_section
    

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk':self.class_codes})

class Post (models.Model):
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    # post=models.TextField(max_length=1000)
    post=RichTextUploadingField(blank=True,null=True)
    userID=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    comment = models.ForeignKey('Post', null=True, related_name= "comments", on_delete=models.CASCADE )
    # date_added=models.DateTimeField(auto_now_add=True,null=True)





class student_classroom(models.Model):
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE)

    
class exam(models.Model):
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    exam_title=models.CharField(max_length=20,null=True)
    exam_post=RichTextUploadingField(blank=True,null=True)
    faculty=models.ForeignKey(User,on_delete=models.CASCADE,default=None)   
    total_marks=models.IntegerField(null=True)
    exam_time=models.DateTimeField()



class student_submission(models.Model):
    student_input=RichTextUploadingField(blank=True,null=True)
    student_post_time=models.DateTimeField(auto_now_add=True,null=True)
    exam = models.ForeignKey(exam,on_delete=models.CASCADE)
    obtained_marks = models.CharField(max_length=20,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('exam_detail', kwargs={'pk':id})