#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.urls import path, include
from students.views import StudentRegistrationAPIView, StudentLoginAPIView, StudentLogoutAPIView
from rest_framework.routers import SimpleRouter
from students.views import StudentViewSet


app_name = 'students'
crud_router = SimpleRouter()
crud_router.register('', StudentViewSet, basename="students")
urlpatterns = [
    # authen
    path('register/', StudentRegistrationAPIView.as_view(),
         name='student-register-api'),
    path('login/', StudentLoginAPIView.as_view(), name='student-login-api'),
    path('logout/', StudentLogoutAPIView.as_view(), name='-student-logout-api'),
    # crud
    path('', include(crud_router.urls))
]
