from django.shortcuts import render
from rest_framework import serializers
from recruiters.models import Recruiter
# Create your views here.

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ('id', 'name', 'company')
        


