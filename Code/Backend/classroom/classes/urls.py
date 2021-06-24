from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns =[
   path('create',views.createCourse,name='createCourse'),
   path('course_detail/<str:pk>/',views.courseDetail, name='course_detail'),
   path('course_edit/<str:pk>/',views.courseEdit, name='course_edit'),
   path('course_delete/<str:pk>/',views.courseDelete, name='course_delete'),
   path('join_class',views.joinclass,name='join_class'),
]