from django.utils import timezone
from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=200, min_length=2)
    answer = models.IntegerField()
