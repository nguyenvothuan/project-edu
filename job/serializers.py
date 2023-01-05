from django.shortcuts import render
from rest_framework import serializers
from job.models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('email', 'company', 'title', 'job_type', 'description', 'salary', 'last_date', 'is_published', 'is_closed', 'timestamp')
        
        