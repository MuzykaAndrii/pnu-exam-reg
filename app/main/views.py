import json

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.views import APIView

from participants.models import Participant
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

        if not participant_form.is_valid():
            return render(request, "main/register.html",
                context={
                    "data": self.get_exams_tree_json(),
                    "participant_form": participant_form,
                }
            )
        
        if not admission_form.is_valid():
            messages.error(request, admission_form.non_field_errors())
            messages.error(request, admission_form.errors.as_ul())
            return redirect("exams:register")
        
        participant: Participant = participant_form.save(commit=False)
        participant.candidate_for = admission_form.cleaned_data.get("speciality")
        participant.save()

        messages.success(request, "Ви успішно зареєструвались на екзамен(и), очікуйте подальшу інформацію на електронній пошті")
        return redirect("exams:register")
    

    def get_exams_tree_json(self):
        degrees = Degree.with_non_expired_exams.all()
        serializer = DegreeSerializer(degrees, many=True)
        return json.dumps(serializer.data)



class ExamsEndpoint(APIView):
    def get(self, request: HttpRequest):
        degrees = Degree.with_non_expired_exams.all()
        serializer = DegreeSerializer(degrees, many=True)

        return Response(serializer.data)
