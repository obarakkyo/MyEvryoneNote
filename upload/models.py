from django.db import models
from django.utils import timezone

from lecture.models import LectureModel

def SavePath(instance, filename):
    return f'{instance.lecture_model}/{instance.lecture_choice}/{filename}'

def SavePathImage(instance, image_file):
    return f'images/{instance.lecture_model}/{instance.lecture_choice}/{image_file}'

lecture_choices = [
    ("1st" , "1回目"),
    ("2st" , "2回目"),
    ("3st" , "3回目"),
    ("4st" , "4回目"),
    ("5st" , "5回目"),
    ("6st" , "6回目"),
    ("7st" , "7回目"),
    ("8st" , "8回目"),
    ("9st" , "9回目"),
    ("10st" , "10回目"),
    ("11st" , "11回目"),
    ("12st" , "12回目"),
    ("13st" , "13回目"),
    ("14st" , "14回目"),
]

class UploadModel(models.Model):
    note_title = models.CharField(max_length=255)
    create_user = models.CharField(max_length=128, default="名無しさん")
    file = models.FileField(upload_to=SavePath)
    image_file = models.ImageField(upload_to=SavePathImage)
    create_time = models.DateTimeField(default=timezone.now)
    lecture_choice = models.CharField(max_length=200, choices=lecture_choices, default="1st")
    lecture_model = models.ForeignKey(LectureModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_title