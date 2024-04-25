import json

from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView

from main.forms import AdmissionForm
from participants.forms import ParticipantForm
from main.models import Degree
from main.serializers import DegreeSerializer


class ExamRegisterView(View):
    def get(self, request: HttpRequest):
        data = self.get_exams_tree_json()

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
        participant_form = ParticipantForm(request.POST)
        admission_form = AdmissionForm(request.POST)

        if participant_form.is_valid():
            print(participant_form.cleaned_data)
        
        if admission_form.is_valid():
            print(admission_form.cleaned_data)
    

    def get_exams_tree_json(self):
        degrees = Degree.with_non_expired_exams.all()
        serializer = DegreeSerializer(degrees, many=True)
        return json.dumps(serializer.data)



class ExamsEndpoint(APIView):
    def get(self, request: HttpRequest):
        degrees = Degree.with_non_expired_exams.all()
        serializer = DegreeSerializer(degrees, many=True)

        return Response(serializer.data)
