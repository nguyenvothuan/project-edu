from accounts.views import RegistrationAPIView, LoginView, LogoutView
from .models import Advisor, VerifiedAdvisor
from .serializers import AdvisorSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from rest_framework import permissions

class IsVerified(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and verified
        if not request.user.is_authenticated:
            return False
        verified_users = VerifiedAdvisor.objects.filter(user=request.user, is_verified=True)
        return verified_users.exists()

#Authentication:
class AdvisorRegistrationAPIView(RegistrationAPIView):
    role = 'is_advisor'
    sub_model_class = Advisor
    sub_model_classname = 'advisor'
    __doc__ = "Registration API for advisor"

class AdvisorLoginAPIView(LoginView):
    role = 'is_advisor'
    role_name = 'advisor'
    
class AdvisorLogoutAPIView(LogoutView):
    pass

#CRUD

class AdvisorViewSet(ModelViewSet):
    permission_classes = [IsVerified]
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer