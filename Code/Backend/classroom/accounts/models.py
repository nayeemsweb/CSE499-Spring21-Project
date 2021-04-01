from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    Department= [
        ('Accounting & Finance', 'Accounting & Finance'),
        ('Economics', 'Economics'),
        ('Management', 'Management'),
        ('Marketing & International Business', 'Marketing & International Business'),
        ('MBA & EMBA Programs', 'MBA & EMBA Programs'),
        ('Architecture', 'Architecture'),
        ('Civil & Environmental Engineering', 'Civil & Environmental Engineering'),
        ('Electrical & Computer Engineering', 'Electrical & Computer Engineering'),
        ('Mathematics & Physics', 'Mathematics & Physics'),
        ('English & Modern Languages', 'English & Modern Languages'),
        ('Political Science & Sociology', 'Political Science & Sociology'),
        ('Law', 'Law'),
        ('Biochemistry & Microbiology', 'Biochemistry & Microbiology'),
        ('Environmental Science & Management', 'Environmental Science & Management'),
        ('Pharmaceutical Sciences', 'Pharmaceutical Sciences'),
        ('Public Health', 'Public Health'),        
    ]
    is_student = models.BooleanField(default=True)
    is_faculty = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department =models.CharField(max_length=100, choices=Department, default='None')

class StudentProfile(models.Model):      
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key= True) 
    image = models.ImageField(default='default.jpg',upload_to='student_pics')
    studentID = models.CharField(max_length=20)

class FacultyProfile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE,primary_key=True) 
    image = models.ImageField(default='default.jpg',upload_to='faculty_pics')
    facultyID = models.CharField(max_length=20)
    bio = models.CharField(max_length=100)    
    