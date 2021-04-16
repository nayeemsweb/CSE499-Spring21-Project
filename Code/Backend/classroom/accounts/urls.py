from django.urls import path
from .import views

urlpatterns =[
   path('',views.facultyRegistration,),
   path("student", views.StudentRegistration, name='student'),
]