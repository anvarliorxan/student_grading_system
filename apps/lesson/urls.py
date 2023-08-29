from django.urls import path
from apps.lesson.api import *

urlpatterns = [
    path('lessons', LessonListApi.as_view()),
    path('notes', NoteListApi.as_view()),
]
