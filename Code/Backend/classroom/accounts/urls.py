from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from .import views

urlpatterns =[
    path('', views.register, name='register'),
    path('studentRegister/', views.studentRegister.as_view(), name='studentRegister'),
    path('facultyRegister/', views.facultyRegister.as_view(), name='facultyRegister'),
    path('live/', views.live),
]

