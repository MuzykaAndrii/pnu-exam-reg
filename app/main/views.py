from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
import json

from rest_framework.response import Response
from rest_framework.views import APIView

from participants.forms import ParticipantForm
from main.models import Degree
from main.serializers import DegreeSerializer


class ExamRegisterView(View):
    def get(self, request: HttpRequest):
        degrees = Degree.objects.all()
        serializer = DegreeSerializer(degrees, many=True)
        data = json.dumps(serializer.data)

        participant_form = ParticipantForm()
    
        return render(
            request,
            "main/register.html",
            context={
                "data": data,
                "participant_form": participant_form,
            }
        )

    def post(self, request: HttpRequest):
        # handle form
        pass


class ExamsEndpoint(APIView):
    def get(self, request: HttpRequest):
        degrees = Degree.objects.all()

        serializer = DegreeSerializer(degrees, many=True)

        return Response(serializer.data)
