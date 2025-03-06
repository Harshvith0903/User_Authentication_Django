# Create your models here.
from django.db import models

class login(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
