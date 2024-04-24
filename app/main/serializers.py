from rest_framework.serializers import ModelSerializer, CharField, DateTimeField

from main.models import Degree, StudyingArea, Exam, UniversityBuilding


class BuildingSerializer(ModelSerializer):
    class Meta:
        model = UniversityBuilding
        fields = (
            "name",
            "address",
        )


class ExamSerializer(ModelSerializer):
    building = BuildingSerializer()
    type = CharField(source="get_type_display")
    time = DateTimeField(format="%d.%m.%Y %H:%M")

    class Meta:
        model = Exam
        fields = (
            "id",
            "subject",
            "type",
            "audience",
            "time",
            "building",
        )


class StudyingAreaSerializer(ModelSerializer):
    exams = ExamSerializer(many=True)

    class Meta:
        model = StudyingArea
        fields = (
            "id",
            "code",
            "name",
            "exams",
        )


class DegreeSerializer(ModelSerializer):
    areas = StudyingAreaSerializer(many=True)

    class Meta:
        model = Degree
        fields = (
            "id",
            "name",
            "weight",
            "areas",
        )