#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.urls import path,include

# Rest Framework imports.

# Third Party Library imports

# local imports.
from accounts.views import (
                          RegistrationAPIView,
                          UserAPIView,
                          LoginView,
                          LogoutView,
                          ChangePasswordView,
                          )

app_name = 'accounts'

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register-api'),
    path('login/', LoginView.as_view(), name='login-api'),
    path('logout/', LogoutView.as_view(), name='logout-api'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password-api'),
    path('list/users/', UserAPIView.as_view(), name='user-api'),
    path('students/', include("students.urls", namespace="accounts-students-api")),
    path('recruiters/',include("recruiters.urls", namespace="recruiters-students-api")),
]
