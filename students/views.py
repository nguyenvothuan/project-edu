from accounts.views import RegistrationAPIView
from students.models import Student
# Create your views here.

class StudentRegistrationAPIView(RegistrationAPIView):
    role = 'is_student'
    sub_model_class = Student
    sub_model_classname = 'student'
    