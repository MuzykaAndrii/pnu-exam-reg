from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from main.models import Degree
from main.serializers import DegreeSerializer


class ExamRegisterView(View):
    def get(self, request: HttpRequest):
        return render(request, "main/register.html")

    def post(self, request: HttpRequest):
        # handle form
        pass


class ExamsEndpoint(APIView):
    def get(self, request: HttpRequest):
        degrees = Degree.objects.all()

        serializer = DegreeSerializer(degrees, many=True)

        return Response(serializer.data)
