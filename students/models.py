from django.utils.translation import gettext_lazy as _
from django.db import models
from schools.models import School

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    
