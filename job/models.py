# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Job(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    company = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    applicants = models.ManyToManyField('students.Student', blank=True)