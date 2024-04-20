from django.db import models


class Degree(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Назва ступеня",
        null=False,
        blank=False,
    )
    weight = models.FloatField(
        verbose_name="Вага ступеня",
        blank=False,
        null=False,
    )


class StudyingArea(models.Model):
    code = models.FloatField(
        verbose_name="Код спеціальності / ОП"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Спеціальність / Освітня програма",
        null=False,
        blank=False,
    )
    degree = models.ForeignKey(
        Degree,
        verbose_name="Ступінь",
        related_name="areas",
        on_delete=models.CASCADE,
    )


class ExamForms(models.IntegerChoices):
    FACE_TO_FACE = 1, "Очно"
    REMOTE = 2, "Дистанційно"


class ExamTypes(models.IntegerChoices):
    TESTING = 1, "Тестування"
    IN_WRITING = 2, "Письмово"
    ORALLY = 3, "Усно"


class UniversityBuilding(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Назва корпусу",
        null=False,
        blank=False,
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адреса корпусу",
        null=False,
        blank=False,
    )


class Exam(models.Model):
    subject = models.CharField(
        max_length=150,
        verbose_name="Предмет",
    )
    form = models.PositiveSmallIntegerField(
        verbose_name="Форма проведення екзамену",
        choices=ExamForms.choices,
    )
    type = models.PositiveSmallIntegerField(
        verbose_name="Тип екзамену",
        choices=ExamTypes.choices,
    )
    building = models.ForeignKey(
        UniversityBuilding,
        verbose_name="Корпус університету",
        related_name="exams",
        on_delete=models.CASCADE,
    )
    audience = models.CharField(
        max_length=50,
        verbose_name="Номер аудиторії",
        blank=True,
        null=True,
    )
    time = models.DateTimeField(
        verbose_name="Дата і час екзамену",
        null=False,
        blank=False,
    )
