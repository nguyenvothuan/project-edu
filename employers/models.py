from django.db import models
from django.utils.translation import gettext_lazy as _
from companies.models import Company
# Create your models here.

class Employer(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    
    