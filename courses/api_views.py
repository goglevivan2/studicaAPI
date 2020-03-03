from rest_framework import viewsets
from . import models
from . import serializers

class UsersViewset(viewsets.ModelViewSet):
    queryset = models.Users.objects.all()
    serializer_class = serializers.UsersSerializer

class CourseViewset(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class Comment_CourseViewset(viewsets.ModelViewSet):
    queryset = models.Comment_Course.objects.all()
    serializer_class = serializers.Comment_CourseSerializer

class StudentsViewset(viewsets.ModelViewSet):
    queryset = models.Students.objects.all()
    serializer_class = serializers.StudentsSerializer

class ProfsViewset(viewsets.ModelViewSet):
    queryset = models.Profs.objects.all()
    serializer_class = serializers.ProfsSerializer


class LessonsViewset(viewsets.ModelViewSet):
    queryset = models.Lessons.objects.all()
    serializer_class = serializers.LessonsSerializer


class HomeworkViewset(viewsets.ModelViewSet):
    queryset = models.Homework.objects.all()
    serializer_class = serializers.HomeworkSerializer


class AnswersViewset(viewsets.ModelViewSet):
    queryset = models.Answers.objects.all()
    serializer_class = serializers.AnswersSerializer


class Comment_AnswersViewset(viewsets.ModelViewSet):
    queryset = models.Comment_Answers.objects.Comment_AnswersSerializer



