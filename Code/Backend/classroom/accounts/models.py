from django.db import models
from django.contrib.auth.models import User

class department (models.Model):
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
    name = models.CharField(max_length=200, choices=Department)

    def __str__(self):
        return self.name
class student (models.Model):
    user = models.OneToOneField(User, null=True, blank= True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    studentID = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(department, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.name


class faculty (models.Model):
    user = models.OneToOneField(User, null=True, blank= True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    facultyID = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    initials = models.CharField(max_length=10)
    bio = models.CharField(max_length=500)
    department = models.ForeignKey(department, null=True, on_delete= models.SET_NULL)


    def __str__(self):
        return self.name






