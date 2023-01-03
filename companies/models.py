from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    description = models.TextField(max_length=1000) 