from django.db import models
from students.models import Student
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    description = models.TextField(max_length=10000) 
    # stored the students who are following this companies
    followers = models.ManyToManyField(Student, through='observers.Follow', related_name='following_companies') 
    
