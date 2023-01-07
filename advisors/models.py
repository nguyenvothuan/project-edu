from django.utils.translation import gettext_lazy as _
from django.db import models
from schools.models import School
# Create your models here.

class Advisor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    is_verified = models.BooleanField(default=False)

# class VerifiedAdvisor(models.Model):
#     user = models.ForeignKey(Advisor, on_delete=models.CASCADE)
#     is_verified = models.BooleanField(default=False)
#     verification_reason = models.TextField()
