from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns =[
   path('create',views.createCourse,name='createCourse'),
   path('course_detail/<str:pk>/',views.courseDetail, name='course_detail'),
]