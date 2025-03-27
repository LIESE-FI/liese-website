# Generated by Django 5.1.6 on 2025-03-20 03:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.member'),
        ),
        migrations.AlterField(
            model_name='opportunityrequest',
            name='opportunity_type',
            field=models.CharField(choices=[('investigacion', 'Investigación'), ('tesis', 'Tesis'), ('maestria', 'Programas de Maestría'), ('servicio', 'Servicio Social')], max_length=50, null=True),
        ),
    ]
