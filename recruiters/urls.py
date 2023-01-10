#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.urls import path, include
from recruiters.views import *

from rest_framework.routers import SimpleRouter


app_name = 'students'
crud_router = SimpleRouter()
crud_router.register('', recruiterViewSet, basename="recruiters")
urlpatterns = [
    # authen
    path('register/', recruiterRegistrationAPIView.as_view(),
         name='recruiter-register-api'),
    path('login/', recruiterLoginAPIView.as_view(), name='recruiter-login-api'),
    path('logout/', recruiterLogoutAPIView.as_view(), name='recruiter-logout-api'),
    # crud
    path('', include(crud_router.urls)),
]
