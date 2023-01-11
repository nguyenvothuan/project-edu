from rest_framework.response import Response
from accounts.views import RegistrationAPIView, LoginView, LogoutView, APIView
from students.models import Student
from rest_framework.viewsets import ModelViewSet
from students.serializers import StudentSerializer, StudentFollowCompanySerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

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

#CRUD

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Follow/Unfollow
class FollowCompany(APIView):
    http_method_names = ['post', 'delete']
    serializer = StudentFollowCompanySerializer
    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Change Password API",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'old_password': openapi.Schema(type=openapi.TYPE_STRING),
                'new_password': openapi.Schema(type=openapi.TYPE_STRING)
            },
            required=['old_password', 'new_password']
        ),
        responses={
            200: openapi.Response('Success', openapi.Schema(type=openapi.TYPE_OBJECT)),
            400: openapi.Response('Bad request', openapi.Schema(type=openapi.TYPE_OBJECT)),
        },

    )
    def put(self,request,*args, **kwargs):
        """Follow a Company"""
        try:
            pass
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
    
class UnfollowCompany(APIView):
    http_method_names = ['put']