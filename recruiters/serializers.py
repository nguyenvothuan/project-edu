from django.shortcuts import render
from rest_framework import serializers
from recruiters.models import recruiter
# Create your views here.

class recruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = recruiter
        fields = ('id', 'name', 'company')
        


