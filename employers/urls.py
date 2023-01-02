#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.urls import path,include
from employers.views import *

from accounts.swagger import schema_view




app_name = 'students'

urlpatterns = [
    path('register/', EmployerRegistrationAPIView.as_view(), name='employer-register-api'),
    path('login/', EmployerLoginAPIView.as_view(), name='employer-login-api'),
    path('logout/',EmployerLogoutAPIView.as_view(), name='employer-logout-api'),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="schema_view"),
    # path('list/users/', UserAPIView.as_view(), name='user-api'),
]
