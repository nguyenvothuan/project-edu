from django.shortcuts import render
from rest_framework import serializers
from schools.models import School
# Create your views here.

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name')
        