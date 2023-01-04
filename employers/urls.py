#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.urls import path, include
from employers.views import *

from rest_framework.routers import SimpleRouter


app_name = 'students'
crud_router = SimpleRouter()
crud_router.register('', EmployerViewSet, basename="employers")
urlpatterns = [
    # authen
    path('register/', EmployerRegistrationAPIView.as_view(),
         name='employer-register-api'),
    path('login/', EmployerLoginAPIView.as_view(), name='employer-login-api'),
    path('logout/', EmployerLogoutAPIView.as_view(), name='employer-logout-api'),
    # crud
    path('', include(crud_router.urls)),
]
