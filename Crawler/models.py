from django.db import models

class Notice(models.Model):
    num = models.IntegerField() # nullable 할 수 없게 설정해야 됨
    title = models.TextField()
    location = models.CharField(max_length=20)