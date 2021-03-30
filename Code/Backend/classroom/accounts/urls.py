from django.urls import path
from .import views

urlpatterns =[
    path('', views.student_profile_signup, name='SignUp')
]