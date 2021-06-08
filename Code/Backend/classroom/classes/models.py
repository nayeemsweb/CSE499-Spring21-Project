from django.db import models
from django.contrib.auth.models import User
from accounts.models import Faculty
import uuid
class Classroom (models.Model):
    facultyiD=models.OneToOneField(Faculty, on_delete= models.CASCADE)
    class_code=models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    class_pics=models.ImageField(null=True, blank=True)
    course_title=models.CharField(max_length=20)
    course_subtitle=models.CharField(max_length=20,null=True)
    course_description=models.CharField(max_length=500,null=True)
    

class Post (models.Model):
    class_code=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    post=models.CharField(max_length=1000)
    userID=models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    postID=models.ForeignKey(Post, on_delete= models.CASCADE)
    comments=models.CharField(max_length=1000)
    userID=models.ForeignKey(User,on_delete=models.CASCADE)



