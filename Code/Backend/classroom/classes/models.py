from django import db
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Faculty
import uuid
import random
import string

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
    # class Meta:
    #     db_table="Classes"
    # def __str__(self):
    #     return self.facultyiD

class Post (models.Model):
    class_code=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    post=models.CharField(max_length=1000)
    userID=models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    postID=models.ForeignKey(Post, on_delete= models.CASCADE)
    comments=models.CharField(max_length=1000)
    userID=models.ForeignKey(User,on_delete=models.CASCADE)
# class MyUUIDModel(models.Model):
#     id = models.UUIDField(
#          primary_key = True,
#          default = uuid.uuid4,
#          editable = False)


