# Generated by Django 3.2 on 2022-01-10 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GL', '0002_rename_locataire_location_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='client',
            new_name='Locataire',
        ),
        migrations.AlterField(
            model_name='location',
            name='NumLocat',
            field=models.CharField(max_length=39),
        ),
    ]
