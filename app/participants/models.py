from django.db import models

from main.models import StudyingArea


class Participant(models.Model):
    firstname = models.CharField(
        verbose_name="Імя",
        max_length=50,
        null=False,
        blank=False,
    )
    lastname = models.CharField(
        verbose_name="Прізвище",
        max_length=50,
        null=False,
        blank=False,
    )
    surname = models.CharField(
        verbose_name="По батькові",
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        verbose_name="Електронна пошта",
        null=False,
        blank=False,
    )
    phone = models.CharField(
        verbose_name="Номер телефону",
        max_length=20,
        null=True,
        blank=True,
    )
    candidate_for = models.ForeignKey(
        StudyingArea,
        on_delete=models.CASCADE,
        verbose_name="Кандидат на",
        related_name="participants",
        blank=True,
        null=False,
    )

    @property
    def fullname(self):
        return f"{self.lastname} {self.firstname} {self.surname}"

    def __str__(self) -> str:
        return f"{self.fullname} {self.candidate_for}"

    class Meta:
        verbose_name = "Учасник"
        verbose_name_plural = "Учасники"