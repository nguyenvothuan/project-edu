from accounts.views import RegistrationAPIView
# Create your views here.

class StudentRegistrationAPIView(RegistrationAPIView):
    role = 'is_student'

