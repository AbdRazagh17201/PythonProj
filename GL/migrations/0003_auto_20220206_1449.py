# Generated by Django 3.2 on 2022-02-06 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GL', '0002_auto_20220206_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrat',
            name='DateContr',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='DateDeb',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='DateFin',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
