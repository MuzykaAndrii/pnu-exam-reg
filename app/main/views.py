from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class ExamRegisterView(View):
    def get(self, request: HttpRequest):
        # retrieve form
        pass

    def post(self, request: HttpRequest):
        # handle form
        pass