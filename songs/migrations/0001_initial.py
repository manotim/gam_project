# Generated by Django 5.1.4 on 2024-12-29 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('song_type', models.CharField(choices=[('audio', 'Audio'), ('video', 'Video')], default='audio', max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='songs/audio/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='songs/video/')),
                ('is_downloadable', models.BooleanField(default=False)),
                ('uploaded_by', models.CharField(blank=True, max_length=255, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
