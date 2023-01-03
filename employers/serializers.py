from django.shortcuts import render
from rest_framework import serializers
from employers.models import Employer
# Create your views here.

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'name', 'company')
        


