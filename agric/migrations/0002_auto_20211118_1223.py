# Generated by Django 3.2.6 on 2021-11-18 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agric', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bio_data',
            old_name='surname_name',
            new_name='surname',
        ),
        migrations.RenameField(
            model_name='historicalbio_data',
            old_name='surname_name',
            new_name='surname',
        ),
    ]
