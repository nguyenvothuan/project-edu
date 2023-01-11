from rest_framework.response import Response
from accounts.views import RegistrationAPIView, LoginView, LogoutView, APIView
from students.models import Student
from companies.models import Company
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

# CRUD


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Follow/Unfollow


class StudentFollowCompany(APIView):
    http_method_names = ['post', 'delete']
    serializer_class = StudentFollowCompanySerializer
    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Change Password API",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'company_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=['company_id']
        ),
        responses={
            200: openapi.Response('Success', openapi.Schema(type=openapi.TYPE_OBJECT)),
            400: openapi.Response('Bad request', openapi.Schema(type=openapi.TYPE_OBJECT)),
        },
    )
    def post(self, request, *args, **kwargs):
        """Follow a Company"""
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                user = request.user
                student = user.student
                company = Company.objects.filter(
                    id=serializer.data.get('company_id')).first()
                company.followers.add(student)
                company.save()
                student.save()
                return Response({"status": "success"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        security=[{'Bearer': []}],
        operation_description="Change Password API",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'company_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=['company_id']
        ),
        responses={
            200: openapi.Response('Success', openapi.Schema(type=openapi.TYPE_OBJECT)),
            400: openapi.Response('Bad request', openapi.Schema(type=openapi.TYPE_OBJECT)),
        },
    )
    def delete(self, request, *args, **kwargs):
        """Unfollow a Company"""
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                user = request.user
                student = user.student
                company = Company.objects.filter(
                    id=serializer.data.get('company_id')).first()
                company.followers.remove(student)
                company.save()
                student.save()
                return Response({"status": "success"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
