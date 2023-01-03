from django.shortcuts import render
from schools.models import School
from schools.serializers import SchoolSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
