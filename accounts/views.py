# python imports
import requests

# Django imports
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth import logout  
from django.db import models
# Rest Framework imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

# local imports
from accounts.models import User, Projects
from accounts.serializers import ( UserCreateSerializer, 
                                    UserListSerializer,     
                                    ProjectsCreateSerializer,
                                    ProjectsListSerializer)
from accounts.utils import generate_jwt_token
from accounts.tasks import add

# Create your views here.


class TestAppAPIView(APIView):

    def get(self, request, format=None):
        try:
            result = add.delay(11, 15)
            print(result)
            return Response({'status': True,
                             'Response': "Successfully Tested"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class RegistrationAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    role = None
    sub_model_class: models.Model = None #can be Student or Employer or School or motherfucker anything you want it to be      
    sub_model_classname = ""
    __doc__ = "Registration API for user"

    def post(self, request, *args, **kwargs):
        try:
            user_serializer = self.serializer_class(data=request.data)
            if user_serializer.is_valid():
                user = user_serializer.save()
                if self.role:
                    setattr(user, self.role, True)
                    sub_model = self.sub_model_class.objects.create(email=request.data['email'])
                    setattr(user, self.sub_model_classname, sub_model)
                    sub_model.save()
                    user.save() 
                data = generate_jwt_token(user, user_serializer.data)
                return Response(data, status=status.HTTP_200_OK)
            else:
                message = ''
                for error in user_serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False,
                             'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
            


class LoginView(JSONWebTokenAPIView):
    role = None
    role_name = ""
    serializer_class = JSONWebTokenSerializer
    __doc__ = "Log In API for user which returns token"
    role = None
    def check_role(self, user):
        if self.role:
            return getattr(user, self.role)
        return False

    # @staticmethod
    def post(self, request):
        try:
            serializer = JSONWebTokenSerializer(data=request.data)
            if serializer.is_valid():
                serialized_data = serializer.validate(request.data)
                user = User.objects.get(email=request.data.get('email'))
                if self.check_role(user):
                    return Response({'status': False,
                                 'message': "Not a %s account" % self.role_name},
                                status=status.HTTP_400_BAD_REQUEST)
                return Response({
                    'status': True,
                    'token': serialized_data['token'],
                }, status=status.HTTP_200_OK)
            else:
                message = ''
                for error in serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, ObjectDoesNotExist):
            return Response({'status': False,
                             'message': "User does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        """
        Logout API for user
        """
        try:
            user = request.user
            logout(request)
            return Response({'status': True,
                             'message': "logout successfully"},
                            status=status.HTTP_200_OK)
        except (AttributeError, ObjectDoesNotExist):
            return Response({'status': False},
                            status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(GenericAPIView):
    serializer_class = UserListSerializer
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        List all the users.
        """
        try:
            users = User.objects.all()
            user_serializer = UserListSerializer(users, many=True)

            users = user_serializer.data
            return Response({'status': True,
                             'Response': users},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class ProjectAPIView(GenericAPIView):
    serializer_class = ProjectsListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        List all the projects.
        """
        try:
            projects = Projects.objects.all()
            project_serializer = ProjectsListSerializer(projects, many=True)

            projects = project_serializer.data
            return Response({'status': True,
                             'Response': projects},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, format=None):
        """
        Create a project
        """
        try:
            data = request.data
            data['user'] = request.user.pk
            serializer = ProjectsCreateSerializer(data=data)
            if serializer.is_valid():
                project = serializer.create(serializer.data)
                return Response({'status': True,
                        'project': project.id,
                        'message': "Project Added Successfully"},
                        status=status.HTTP_200_OK)
            else:
                message = ''
                for error in serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)