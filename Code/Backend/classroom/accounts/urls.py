from django.urls import path
from .import views

urlpatterns =[
   path('',views.FacultyRegistration, name='faculty'),
   path('student', views.StudentRegistration, name='student'),
   path('loginPage',views.login, name='loginPage'),
]