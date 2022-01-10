# Generated by Django 3.2 on 2022-01-10 20:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numcl', models.CharField(max_length=25)),
                ('Nom_Prenom', models.CharField(max_length=255)),
                ('Numero_Permis', models.CharField(max_length=200)),
                ('Adresse', models.CharField(max_length=30)),
                ('Telephon', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immt', models.CharField(max_length=10)),
                ('Modelle', models.CharField(max_length=15)),
                ('Marque', models.CharField(max_length=25)),
                ('Couleur', models.CharField(max_length=30)),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('NumLocat', models.CharField(max_length=25)),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateLocat', models.DateField()),
                ('dureeLocat', models.IntegerField()),
                ('Locataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GL.client')),
                ('voiture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GL.voiture')),
            ],
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumContr', models.CharField(max_length=39)),
                ('DateContr', models.DateTimeField(default=django.utils.timezone.now)),
                ('DateDeb', models.DateTimeField(default=django.utils.timezone.now)),
                ('DateFin', models.DateTimeField(default=django.utils.timezone.now)),
                ('Km_Parcours', models.FloatField()),
                ('Tarif_Par_jour', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GL.client')),
                ('voiture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GL.voiture')),
            ],
        ),
    ]
