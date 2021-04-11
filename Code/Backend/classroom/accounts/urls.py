from django.urls import path
from .import views

urlpatterns =[
    path('', views.studentRegister.as_view(), name='studentRegister'),
    path('facultyRegister/', views.facultyRegister.as_view(), name='facultyRegister'),
]