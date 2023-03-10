from django.shortcuts import render
from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'school')
        
class StudentFollowCompanySerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    