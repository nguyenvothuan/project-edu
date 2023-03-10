from django.db import models
from django.utils.translation import gettext_lazy as _
from companies.models import Company
# Create your models here.

class Recruiter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    
    