from django.db import models
import datetime
from django.utils import timezone


class Users(models.Model):
    TYPE_OF_USERS=(
        ('S','STUDENT'),
        ('P','PROFESSOR')
    )
    users_name=models.CharField('имя ',unique=True,max_length=50)
    users_role = models.CharField('роль пользователя ',max_length=1, choices=TYPE_OF_USERS)
    users_password = models.CharField('пароль ',max_length=128)
    users_email = models.EmailField('почта',unique=True,max_length=128)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Course(models.Model):
    course_name=models.CharField('название курса',max_length=200)
    course_description = models.TextField('описание курса')
    owner=models.ForeignKey(Users,on_delete=models.CASCADE)
    pub_date =models.DateTimeField('дата создания курса')

    def __str__(self):
        return self.course_name

    def was_published_recently(self):
        return self.pub_date >= (timezone.now()-datetime.timedelta(days=2))
    class Meta:
        verbose_name= 'Курс'
        verbose_name_plural = 'Курсы'


class Comment_Course(models.Model):
    FK_course=models.ForeignKey(Course,on_delete=models.CASCADE)
    author_name=models.CharField('имя автора',max_length=50)
    comment_text = models.CharField('текст коментария',max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name= 'Комментарий'
        verbose_name_plural = 'Комментарии'




class Students(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Profs(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

class Lessons(models.Model):
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    lessons_name=models.CharField('название урока ',max_length=50)
    profs_id=models.ForeignKey(Profs,on_delete=models.CASCADE)
    lessons_file=models.FileField('файл урока')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Homework(models.Model):
    homework_descript = models.TextField('описание д/з')
    lesson_id = models.ForeignKey(Lessons,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Задание на дом'
        verbose_name_plural = 'Задания на дом'

class Answers(models.Model):
    answers_content=models.TextField('Информация ответа')
    user_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    answers_rate=models.IntegerField('оценка')
    profs_id = models.ForeignKey(Profs,on_delete=models.CASCADE)
    homework_id = models.ForeignKey(Homework,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Comment_Answers(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    text=models.TextField('Комментарий к ответу')
    answer_id = models.ForeignKey(Answers,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий к ответам'
        verbose_name_plural = 'Комментарии к ответам'


