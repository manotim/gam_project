# Generated by Django 5.1.4 on 2024-12-30 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choir', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singer',
            name='audio_song',
        ),
        migrations.RemoveField(
            model_name='singer',
            name='video_song',
        ),
    ]
