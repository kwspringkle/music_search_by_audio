# Generated by Django 5.0.8 on 2024-09-05 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaded_audio',
            name='uploaded_audio_name',
            field=models.TextField(null=True),
        ),
    ]
