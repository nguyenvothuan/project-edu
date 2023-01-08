#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.urls import path,include
from job import views
from rest_framework.routers import SimpleRouter

from accounts.swagger import schema_view
from job.views import JobViewSet
crud_router = SimpleRouter()
crud_router.register('', JobViewSet, basename="job")

app_name = 'Job'

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('', include(crud_router.urls))
    # path('jobs/', views.job_list_View, name='job-list'),
    # path('job/create/', views.create_job_View, name='create-job'),
    # path('job/<int:id>/', views.single_job_view, name='single-job'),
    # path('apply-job/<int:id>/', views.apply_job_view, name='apply-job'),
    # path('about/', views.single_job_view, name='about'),
    # path('contact/', views.single_job_view, name='contact'),
    # path('result/', views.search_result_view, name='search_result'),
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    # path('dashboard/employer/job/<int:id>/applicants/', views.all_applicants_view, name='applicants'),
    # path('dashboard/employer/job/edit/<int:id>', views.job_edit_view, name='edit-job'),
    # path('dashboard/employer/applicant/<int:id>/', views.applicant_details_view, name='applicant-details'),
    # path('dashboard/employer/close/<int:id>/', views.make_complete_job_view, name='complete'),
    # path('dashboard/employer/delete/<int:id>/', views.delete_job_view, name='delete'),
    # path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="schema_view"),
    # path('list/users/', UserAPIView.as_view(), name='user-api'),
]
