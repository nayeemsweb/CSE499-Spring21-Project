from django.contrib import admin
from .models import StudentProfile, FacultyProfile

# Register your models here.
admin.site.Register(StudentProfile)
admin.site.Register(FacultyProfile)