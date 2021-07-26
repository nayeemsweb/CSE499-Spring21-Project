from classes.models import ClassTime,Classroom,Post, student_classroom,exam,student_submission
from django.contrib import admin

# Register your models here.
admin.site.register(ClassTime)
admin.site.register(Classroom)
admin.site.register(Post)
admin.site.register(student_classroom)
admin.site.register(student_submission)
admin.site.register(exam)