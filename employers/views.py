from accounts.views import RegistrationAPIView, LoginView, LogoutView
from employers.models import Employer
# Create your views here.

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