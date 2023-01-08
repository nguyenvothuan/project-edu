from django.shortcuts import render
from rest_framework import serializers
from .models import Advisor
# Create your views here.

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id', 'name', 'school')
        


