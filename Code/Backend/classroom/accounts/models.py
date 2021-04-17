from django.db import models
from django.contrib.auth.models import User

class Department (models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
class Student (models.Model):
    user = models.OneToOneField(User, null=True, blank= True, on_delete= models.CASCADE)
    studentID = models.CharField(max_length=20, null=True)
    department = models.ForeignKey(Department, null=True, on_delete= models.SET_NULL)

    def __str__(self) -> str:
        return self.studentID


class Faculty (models.Model):
    user = models.OneToOneField(User, null=True, blank= True, on_delete= models.CASCADE)
    facultyID = models.CharField(max_length=20)
    bio = models.CharField(max_length=500)
    department = models.ForeignKey(Department, null=True, on_delete= models.SET_NULL)


    def __str__(self):
        return self.facultyID
