from django.db import models

class LectureModel(models.Model):
    name = models.CharField(max_length=255)
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    title4 = models.CharField(max_length=255)
    title5 = models.CharField(max_length=255)
    title6 = models.CharField(max_length=255)
    title7 = models.CharField(max_length=255)
    title8 = models.CharField(max_length=255)
    title9 = models.CharField(max_length=255)
    title10 = models.CharField(max_length=255)
    title11= models.CharField(max_length=255)
    title12 = models.CharField(max_length=255)
    title13= models.CharField(max_length=255)
    title14 = models.CharField(max_length=255)

    def __str__(self):
        return self.name

