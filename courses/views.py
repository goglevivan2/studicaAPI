from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from.models import *
from rest_framework import viewsets

class CourseView(APIView):
    def get(self, request):
        all_courses = Course.objects.all()
        serializer = CourseSerializer(all_courses,many=True)
        return Response({"courses":serializer.data})


class UsersView(APIView):
    def get(self, request):
        all = Users.objects.all()
        serializer = UsersSerializer(all,many=True)
        return Response({"users":serializer.data})

class HomeworkView(APIView):
    def get(self, request):
        all = Homework.objects.all()
        serializer = HomeworkSerializer(all,many=True)
        return Response({"homework":serializer.data})
class HomeworkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class AnswersView(APIView):
    def get(self, request):
        all = Answers.objects.all()
        serializer = AnswersSerializer(all,many=True)
        return Response({"answers":serializer.data})

class AnswersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Answers.objects.all()
    serializer = AnswersSerializer



class StudentsView(APIView):
    def get(self, request):
        all = Students.objects.all()
        serializer = StudentsSerializer(all,many=True)
        return Response({"students":serializer.data})


class ProfsView(APIView):
    def get(self, request):
        all = Profs.objects.all()
        serializer = ProfsSerializer(all,many=True)
        return Response({"profs":serializer.data})
# Create your views here.

class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class CreateCourseView(CreateModelMixin, GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({'details': 'success'})

        user = serializer.validated_data['user']

        return Response({'id': user.id, 'name':user.users_name})