# Generated by Django 5.1.6 on 2025-03-15 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_opportunityrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunityrequest',
            name='opportunity_type',
            field=models.CharField(choices=[('investigacion', 'Investigación'), ('tesis', 'Tesis'), ('maestria', 'Programas de Maestría'), ('servicio_social', 'Servicio Social')], max_length=50, null=True),
        ),
    ]
