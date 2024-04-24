from django.db import models


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