from django.contrib import admin
from .models import student, faculty

# Register your models here.
admin.site.register(student)
admin.site.register(faculty)