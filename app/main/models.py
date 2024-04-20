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

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Науковий ступінь"
        verbose_name_plural = "Наукові ступені"


class StudyingArea(models.Model):
    code = models.CharField(
        max_length=30,
        verbose_name="Код спеціальності / ОП"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Імя",
        null=False,
        blank=False,
    )
    degree = models.ForeignKey(
        Degree,
        verbose_name="Ступінь",
        related_name="areas",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.code} {self.name} | {self.degree}"
    
    class Meta:
        verbose_name = "Спеціальність / ОП"
        verbose_name_plural = "Спеціальності / ОП"


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

    def __str__(self) -> str:
        return f"{self.name} вул. {self.address}"
    
    class Meta:
        verbose_name = "Корпус"
        verbose_name_plural = "Корпуси університету"


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
    target = models.ForeignKey(
        StudyingArea,
        verbose_name="На спеціальінсть",
        related_name="exams",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.target} {self.subject} {self.time}"
    
    class Meta:
        verbose_name = "Екзамен"
        verbose_name_plural = "Екзамени"
