from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', include("apps.student.urls")),
    path('api/lesson/', include("apps.lesson.urls")),
]
