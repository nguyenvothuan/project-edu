from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from job.models import Job
from rest_framework.viewsets import ModelViewSet
from job.serializers import JobSerializer

from django.contrib import messages
from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect, JsonResponse
# from django.core.serializers import serialize
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache

from students.models import Student
from companies.models import Company
from job.forms import *
from job.models import *
# from job.permission import *
Student = get_user_model()


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


def home_view(request):

    published_jobs = Job.objects.filter(
        is_published=True).order_by('-timestamp')
    jobs = published_jobs.filter(is_closed=False)
    total_candidates = Student.objects.count()
    total_companies = Company.objects.count()
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    if request.is_ajax():
        job_lists = []
        job_objects_list = page_obj.object_list.values()
        for job_list in job_objects_list:
            job_lists.append(job_list)

        next_page_number = None
        if page_obj.has_next():
            next_page_number = page_obj.next_page_number()

        prev_page_number = None
        if page_obj.has_previous():
            prev_page_number = page_obj.previous_page_number()

        data = {
            'job_lists': job_lists,
            'current_page_no': page_obj.number,
            'next_page_number': next_page_number,
            'no_of_page': paginator.num_pages,
            'prev_page_number': prev_page_number
        }
        return JsonResponse(data)

    context = {
        'total_candidates': total_candidates,
        'total_companies': total_companies,
        'total_jobs': len(jobs),
        'total_completed_jobs': len(published_jobs.filter(is_closed=True)),
        'page_obj': page_obj
    }
    print('ok')
    # return render(request, 'jobapp/index.html', context)

# @cache_page(60 * 15)
# def job_list_View(request):
#     """
#     """
#     job_list = Job.objects.filter(is_published=True,is_closed=False).order_by('-timestamp')
#     paginator = Paginator(job_list, 12)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {

#         'page_obj': page_obj,

#     }
#     return render(request, 'jobapp/job-list.html', context)
