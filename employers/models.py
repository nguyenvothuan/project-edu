from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Employer(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    company = models.CharField(max_length=100, blank=True)
    