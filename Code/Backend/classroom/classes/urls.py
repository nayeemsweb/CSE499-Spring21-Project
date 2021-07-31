from django.urls import path
from django.urls.conf import include
from .import views
from django.conf.urls import url, include
from django.views.i18n import JavaScriptCatalog
urlpatterns =[
   path('create',views.createCourse,name='createCourse'),
   path('course_detail/<str:pk>/',views.courseDetail, name='course_detail'),
   path('course_edit/<str:pk>/',views.courseEdit, name='course_edit'),
   path('course_delete/<str:pk>/',views.courseDelete, name='course_delete'),
   path('join_class',views.joinclass,name='join_class'),

   path('exam_detail/<int:pk>/',views.examDetails,name='exam_detail'),
   path('submission_edit/<int:pk>/',views.submissionEdit,name='submission_edit'),
   path('mark_submission/<int:pk>/',views.markSubmission,name='mark_submission'),
   url(r'^ckeditor/', include('ckeditor_uploader.urls')),
   path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
]

    