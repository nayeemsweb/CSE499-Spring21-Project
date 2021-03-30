from django.urls import path
from .import views

urlpatterns =[
    path('signup/', views.student_profile_signup, name='')
]