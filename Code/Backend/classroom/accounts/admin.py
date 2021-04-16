from django.contrib import admin
from .models import student, faculty, department

# Register your models here.
admin.site.register(department)
admin.site.register(student)
admin.site.register(faculty)