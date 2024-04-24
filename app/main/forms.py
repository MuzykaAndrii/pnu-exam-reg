from django import forms

from main.models import Degree, StudyingArea


class AdmissionForm(forms.Form):
    base = forms.ModelChoiceField(
        queryset=Degree.objects.all(),
        required=True,
    )
    target = forms.ModelChoiceField(
        queryset=Degree.objects.all(),
        required=True,
    )
    speciality = forms.ModelChoiceField(
        queryset=StudyingArea.objects.all(),
        required=True,
    )