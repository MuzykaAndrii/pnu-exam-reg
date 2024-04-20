from django.urls import path

from main.views import ExamRegisterView


app_name = "exams"


urlpatterns = [
    path("register/", ExamRegisterView.as_view(), name="register"),
]
