from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)

