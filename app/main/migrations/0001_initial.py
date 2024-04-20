# Generated by Django 5.0.4 on 2024-04-20 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва ступеня')),
                ('weight', models.FloatField(verbose_name='Вага ступеня')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва корпусу')),
                ('address', models.CharField(max_length=255, verbose_name='Адреса корпусу')),
            ],
        ),
        migrations.CreateModel(
            name='StudyingArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.FloatField(verbose_name='Код спеціальності / ОП')),
                ('name', models.CharField(max_length=150, verbose_name='Спеціальність / Освітня програма')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='main.degree', verbose_name='Ступінь')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150, verbose_name='Предмет')),
                ('form', models.PositiveSmallIntegerField(choices=[(1, 'Очно'), (2, 'Дистанційно')], verbose_name='Форма проведення екзамену')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Тестування'), (2, 'Письмово'), (3, 'Усно')], verbose_name='Тип екзамену')),
                ('audience', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер аудиторії')),
                ('time', models.DateTimeField(verbose_name='Дата і час екзамену')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='main.universitybuilding', verbose_name='Корпус університету')),
            ],
        ),
    ]
