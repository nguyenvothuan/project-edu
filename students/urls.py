#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.urls import path,include
from students.views import StudentRegistrationAPIView, StudentLoginAPIView
from accounts.swagger import schema_view




app_name = 'students'

urlpatterns = [
    path('register/', StudentRegistrationAPIView.as_view(), name='student-register-api'),
    path('login/', StudentLoginAPIView.as_view(), name='student-login-api'),
    # path('logout/', LogoutView.as_view(), name='logout-api'),
    # path('list/users/', UserAPIView.as_view(), name='user-api'),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="schema_view"),
]
