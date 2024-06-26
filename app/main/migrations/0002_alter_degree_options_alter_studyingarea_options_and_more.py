# Generated by Django 5.0.4 on 2024-04-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='degree',
            options={'verbose_name': 'Науковий ступінь', 'verbose_name_plural': 'Наукові ступені'},
        ),
        migrations.AlterModelOptions(
            name='studyingarea',
            options={'verbose_name': 'Спеціальність / ОП', 'verbose_name_plural': 'Спеціальності / ОП'},
        ),
        migrations.AlterModelOptions(
            name='universitybuilding',
            options={'verbose_name': 'Корпус', 'verbose_name_plural': 'Корпуси університету'},
        ),
        migrations.AlterField(
            model_name='studyingarea',
            name='code',
            field=models.CharField(max_length=30, verbose_name='Код спеціальності / ОП'),
        ),
        migrations.AlterField(
            model_name='studyingarea',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Імя'),
        ),
    ]
