from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate, get_user_model

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ('id', 'users_name','users_role','users_password','users_email')
        write_only_fields = ('users_password','users_email',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        return models.Users.objects.create(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ('id', 'users_name','users_password')

    users_name = serializers.CharField(max_length=50)
    users_password = serializers.CharField(max_length=128, style={'input_type': 'password'},
                         write_only=True)

    def validate(self, data):
        users_name = data.get('users_name', None)
        users_password = data.get('users_password', None)

        if users_name and users_password:
            user = authenticate(users_name=users_name, users_password=users_password)

            if user is None:
                raise serializers.ValidationError(
                    'Provided credentials don\'t match any existing user')

        else:
            raise serializers.ValidationError(
                'Both username and password are required for authentication')

        data['user'] = user
        return data

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'course_name','course_description','owner','pub_date')

    def create(self, validated_data):
        return models.Course.objects.create(**validated_data)

class Comment_CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment_Course
        fields = ('id', 'FK_course','author_name','comment_text')

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = ('user_id', 'course_id')


class ProfsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profs
        fields = ('user_id', 'course_id')

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lessons
        fields = ('course_id', 'lessons_name','profs_id','lessons_file')

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Homework
        fields = ('homework_descript', 'lesson_id')

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answers
        fields = ('answers_content', 'user_id','answers_rate','profs_id','homework_id')

class Comment_AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment_Answers
        fields = ('user_id', 'text','answer_id')


