from django.db import models
from django.contrib.auth.models import User
from ..accounts.models import *

class Classroom (models.Model):
    facultyID=models.ForeignKey(Faculty.facultyID)
    class_code=models.CharField(max_length=20)
    class_pics=models.ImageField(null=True, blank=True)
    course_title=models.CharField(max_length=20)
    course_subtitle=models.CharField(max_length=20,null=True)
    course_description=models.CharField(max_length=500,null=True)
    fb_link=models.CharField(max_length=200,null=True)
    discord_link=models.CharField(max_length=200,null=True)


class Post (models.Model):
    class_code=models.CharField(max_length=20)
    post=models.CharField(max_length=1000)
    like_btn=models.BooleanField()
    userID=models.CharField(max_length=20)

class Comments(models.Model):
    postID=models.ForeignKey(Post)
    comments=models.CharField(max_length=1000)
    userID=models.CharField(max_length=20)



