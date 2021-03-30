from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    is_student = models.BooleanField(default=True)


class StudentProfile(models.Model):
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile') 
    image = models.ImageField(default='default.jpg',upload_to='student_pics')
    studentID = models.CharField(max_length=20, blank=False, primary_key=True)
    department =models.CharField(max_length=100,choices=Department,blank=False,default='None')
    


class FacultyProfile(models.Model):
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
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name= 'faculty_profile') 
    image = models.ImageField(default='default.jpg',upload_to='faculty_pics')
    facultyID = models.CharField(max_length=20,blank=False, primary_key=True)
    bio = models.CharField(max_length=100, blank=False)
    department =models.CharField(max_length=100, choices=Department, blank=False,default='None')
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