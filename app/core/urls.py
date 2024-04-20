from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('exams/', include("main.urls", namespace="exams")),
]
