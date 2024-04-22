from django.urls import path

from main.views import ExamRegisterView, ExamsEndpoint


app_name = "exams"


urlpatterns = [
    path("register/", ExamRegisterView.as_view(), name="register"),
    path("api/", ExamsEndpoint.as_view(), name="api"),
]
