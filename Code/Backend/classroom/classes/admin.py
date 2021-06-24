from classes.models import ClassTime,Classroom, Comment, Post, student_classroom
from django.contrib import admin

# Register your models here.
admin.site.register(ClassTime)
admin.site.register(Classroom)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(student_classroom)