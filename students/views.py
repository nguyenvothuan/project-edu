from accounts.views import RegistrationAPIView, LoginView, LogoutView
from students.models import Student
# Create your views here.

class StudentRegistrationAPIView(RegistrationAPIView):
    role = 'is_student'
    sub_model_class = Student
    sub_model_classname = 'student'
    __doc__ = "Registration API for student"

class StudentLoginAPIView(LoginView):
    role = 'is_student'
    role_name = 'Student'
    
class StudentLogoutAPIView(LogoutView):
    pass