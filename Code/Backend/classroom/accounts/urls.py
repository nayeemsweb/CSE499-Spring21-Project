from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns =[
   path('signup/facutly',views.FacultyRegistration, name='faculty'),
   path('signup/student', views.StudentRegistration, name='student'),
   path('loginPage',views.loginPage, name='loginPage'),
   path('',views.homePage, name='homePage'),
   path('logoutUser', views.logoutUser, name='logoutUser'),
   path('facultyDashboard',views.facultyDashboard, name='facultyDashboard'),
   path('facultyProfile/<int:pk>/',views.facultyProfile,name='facultyProfile'),
   path('studentProfile/<int:pk>/',views.studentProfile ,name='studentProfile'),
]