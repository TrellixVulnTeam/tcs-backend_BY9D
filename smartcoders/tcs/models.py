from django.db import models


# Create your models here.
class trains(models.Model):
    tr_no = models.IntegerField()
    tr_name = models.CharField(max_length = 30)
    dep= models.TimeField(auto_now=False, auto_now_add=False)
    arr = models.TimeField(auto_now=False, auto_now_add=False)
    duration=models.CharField(max_length = 10)
