# Generated by Django 5.0.4 on 2024-04-25 16:16

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_exam_form_alter_exam_audience_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='degree',
            options={'ordering': ('weight',), 'verbose_name': 'Науковий ступінь', 'verbose_name_plural': 'Наукові ступені'},
        ),
        migrations.AlterModelManagers(
            name='exam',
            managers=[
                ('non_expired', django.db.models.manager.Manager()),
            ],
        ),
    ]
