from django.db import models
from students.models import Student
from companies.models import Company
# Create your models here.
class Follow(models.Model):
    date_followed = models.DateTimeField(auto_now_add=True)
    # delete follow if one of the student or company is deleted.
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)