from django.urls import path,include
from .views import*
from rest_framework.routers import DefaultRouter,SimpleRouter

app_name = 'courses'
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('users/', UsersView.as_view()),
    path('profs/', ProfsView.as_view()),
    path('homework/', HomeworkView.as_view()),
    path('answers/', AnswersView.as_view()),
    path('students/', StudentsView.as_view()),
    path('login/', UserLoginView.as_view()),

]

router = DefaultRouter()
router.register(r'createuser', CreateUserView)
router.register(r'homeworkset', HomeworkViewSet)
router.register(r'createcourse', CreateCourseView)
urlpatterns +=router.urls