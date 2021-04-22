from django.urls import path
from .import views

urlpatterns =[
   path('',views.FacultyRegistration, name='faculty'),
   path('student', views.StudentRegistration, name='student'),
   path('loginPage',views.loginPage, name='loginPage'),
   path('homePage',views.homePage, name='homePage'),
   path('logoutUser', views.logoutUser, name='logoutUser'),
   path('facultyDashboard',views.facultyDashboard, name='facultyDashboard'),
]