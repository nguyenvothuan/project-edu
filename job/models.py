# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

Student = get_user_model()

# Create your models here.

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Job(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    company = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    # applicants = models.ManyToManyField('students.Student', blank=True)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    description = models.CharField(max_length=100, blank=True)
    # category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    last_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Applicant(models.Model):

    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title