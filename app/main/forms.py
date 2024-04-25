from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

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

    def clean_speciality(self):
        speciality = self.cleaned_data.get('speciality')  # type: StudyingArea
        exams = speciality.exams.all()

        if not exams or all(exam.is_expired for exam in exams):
            raise ValidationError(
                _("Exams was expired"),
                code="invalid",
            )
        
        return speciality

    def clean(self):
        cleaned_data = super().clean()
        if self.errors: return  # not execute clean if any field error present

        base = cleaned_data.get("base")  # type: Degree
        target = cleaned_data.get("target")  # type: Degree
        speciality = cleaned_data.get("speciality")  # type: StudyingArea

        if target.weight > base.weight + 1:
            raise ValidationError(
                _("You cannot admission to %(target)s having degree %(base)s."),
                code="invalid",
                params={"target": target.name, "base": base.name}
            )

        if speciality.degree_id != target.pk:
            raise ValidationError(
                _("Wrong speciality specified."),
                code="invalid",
            )