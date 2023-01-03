from django.shortcuts import render
from rest_framework import serializers
from companies.models import Company
# Create your views here.

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')
        


