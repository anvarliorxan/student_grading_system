from django.contrib import admin
from apps.lesson.models import Lesson
from apps.lesson.models import Note

admin.site.register(Lesson)
admin.site.register(Note)
