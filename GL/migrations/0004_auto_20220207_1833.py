# Generated by Django 3.2 on 2022-02-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GL', '0003_auto_20220206_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AddField(
            model_name='client',
            name='NomClient',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='NumClient',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='Prenom',
            field=models.CharField(default=3, max_length=25),
            preserve_default=False,
        ),
    ]