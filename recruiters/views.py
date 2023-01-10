from accounts.views import RegistrationAPIView, LoginView, LogoutView
from recruiters.models import recruiter
from recruiters.serializers import recruiterSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

#Authentication:
class recruiterRegistrationAPIView(RegistrationAPIView):
    role = 'is_recruiter'
    sub_model_class = recruiter
    sub_model_classname = 'recruiter'
    __doc__ = "Registration API for recruiter"

class recruiterLoginAPIView(LoginView):
    role = 'is_recruiter'
    role_name = 'recruiter'
    
class recruiterLogoutAPIView(LogoutView):
    pass

#CRUD

class recruiterViewSet(ModelViewSet):
    queryset = recruiter.objects.all()
    serializer_class = recruiterSerializer
