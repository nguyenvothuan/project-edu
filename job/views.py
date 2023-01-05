from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from job.models import Job
from rest_framework.viewsets import ModelViewSet
from job.serializers import JobSerializer

# Create your views here.

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

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