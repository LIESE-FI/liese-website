# Generated by Django 5.1.6 on 2025-03-15 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_member_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpportunityRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('verified', models.BooleanField(default=False)),
                ('verification_token', models.CharField(blank=True, max_length=100, null=True)),
                ('verification_token_expires', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
