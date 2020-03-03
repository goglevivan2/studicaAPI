from django.contrib import admin
from .models import Course,Comment_Course, Users,Students,Profs, Lessons,Homework,Answers,Comment_Answers

admin.site.register(Course)
admin.site.register(Comment_Course)
admin.site.register(Users)
admin.site.register(Students)
admin.site.register(Profs)
admin.site.register(Lessons)
admin.site.register(Homework)
admin.site.register(Answers)
admin.site.register(Comment_Answers)
