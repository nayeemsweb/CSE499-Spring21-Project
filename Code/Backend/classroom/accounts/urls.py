from django.urls import path
from .import views

urlpatterns =[
   path('',views.FacultyRegistration, name='faculty'),
   path('student', views.StudentRegistration, name='student'),
   path('login',views.login, name='login'),
]