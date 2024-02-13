from django.db import models
from lecture.models import LectureModel 
from django.contrib.auth.models import User

# Create your models here.
class BoardModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(LectureModel, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.lecture.name}"
    
    class Meta:
        ordering = ['-created_at']
