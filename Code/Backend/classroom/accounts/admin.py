from django.contrib import admin
from .models import StudentProfile, FacultyProfile

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(FacultyProfile)
