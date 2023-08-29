from django.urls import path
from apps.student.api import *

urlpatterns = [
    path('list', StudentListApi.as_view()),
    path('create', CreateStudentApi.as_view()),
    path('delete/<str:pk>', DeleteStudentApi.as_view()),
    path('update/<str:pk>', UpdateStudentApi.as_view()),
]
