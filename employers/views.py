from accounts.views import RegistrationAPIView, LoginView, LogoutView
from employers.models import Employer
from employers.serializers import EmployerSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

#Authentication:
class EmployerRegistrationAPIView(RegistrationAPIView):
    role = 'is_employer'
    sub_model_class = Employer
    sub_model_classname = 'employer'
    __doc__ = "Registration API for employer"

class EmployerLoginAPIView(LoginView):
    role = 'is_employer'
    role_name = 'employer'
    
class EmployerLogoutAPIView(LogoutView):
    pass

#CRUD

class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer