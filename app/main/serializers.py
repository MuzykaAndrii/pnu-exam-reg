from rest_framework.serializers import ModelSerializer

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

    class Meta:
        model = Exam
        fields = (
            "subject",
            "type",
            "building",
            "audience",
            "time",
        )


class StudyingAreaSerializer(ModelSerializer):
    exams = ExamSerializer(many=True)

    class Meta:
        model = StudyingArea
        fields = (
            "code",
            "name",
            "exams",
        )


class DegreeSerializer(ModelSerializer):
    areas = StudyingAreaSerializer(many=True)

    class Meta:
        model = Degree
        fields = (
            "name",
            "weight",
            "areas",
        )