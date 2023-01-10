from accounts.views import RegistrationAPIView, LoginView, LogoutView
from recruiters.models import Recruiter
from recruiters.serializers import RecruiterSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

#Authentication:
class RecruiterRegistrationAPIView(RegistrationAPIView):
    role = 'is_recruiter'
    sub_model_class = Recruiter
    sub_model_classname = 'recruiter'
    __doc__ = "Registration API for recruiter"

class RecruiterLoginAPIView(LoginView):
    role = 'is_recruiter'
    role_name = 'recruiter'
    
class RecruiterLogoutAPIView(LogoutView):
    pass

#CRUD

class RecruiterViewSet(ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
