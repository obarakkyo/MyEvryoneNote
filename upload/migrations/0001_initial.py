# Generated by Django 5.0.1 on 2024-01-26 05:16

import django.db.models.deletion
import django.utils.timezone
import upload.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_title', models.CharField(max_length=255)),
                ('create_user', models.CharField(default='名無しさん', max_length=128)),
                ('file', models.FileField(upload_to=upload.models.SavePath)),
                ('image_file', models.FileField(upload_to=upload.models.SavePathImage)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('lecture_choice', models.CharField(choices=[('1st', '1回目'), ('2st', '2回目'), ('3st', '3回目'), ('4st', '4回目'), ('5st', '5回目'), ('6st', '6回目'), ('7st', '7回目'), ('8st', '8回目'), ('9st', '9回目'), ('10st', '10回目'), ('11st', '11回目'), ('12st', '12回目'), ('13st', '13回目'), ('14st', '14回目')], default='1st', max_length=200)),
                ('lecture_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecture.lecturemodel')),
            ],
        ),
    ]
