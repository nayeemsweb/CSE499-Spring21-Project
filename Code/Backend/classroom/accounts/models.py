from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    is_student = models.BooleanField(default=True)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile') 
    image = models.ImageField(default='default.jpg',upload_to='student_pics')
    studentID = models.CharField(max_length=20,blank=False)


class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile') 
    image = models.ImageField(default='default.jpg',upload_to='faculty_pics')
    facultyID = models.CharField(max_length=20,blank=False)
    bio = models.CharField(max_length=100, blank=False)