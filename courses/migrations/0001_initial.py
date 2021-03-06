# Generated by Django 3.0.3 on 2020-03-03 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers_content', models.TextField(verbose_name='Информация ответа')),
                ('answers_rate', models.IntegerField(verbose_name='оценка')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200, verbose_name='название курса')),
                ('course_description', models.TextField(verbose_name='описание курса')),
                ('course_owner', models.CharField(max_length=50, verbose_name='автор курса')),
                ('pub_date', models.DateTimeField(verbose_name='дата создания курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_name', models.CharField(max_length=50, unique=True, verbose_name='имя ')),
                ('users_role', models.CharField(choices=[('S', 'STUDENT'), ('P', 'PROFESSOR')], max_length=1, verbose_name='роль пользователя ')),
                ('users_password', models.CharField(max_length=128, verbose_name='пароль ')),
                ('users_email', models.EmailField(max_length=128, unique=True, verbose_name='почта')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Users')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Profs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Users')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessons_name', models.CharField(max_length=50, verbose_name='название урока ')),
                ('lessons_file', models.FileField(upload_to='', verbose_name='файл урока')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('profs_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Profs')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_descript', models.TextField(verbose_name='описание д/з')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lessons')),
            ],
            options={
                'verbose_name': 'Задание на дом',
                'verbose_name_plural': 'Задания на дом',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Users'),
        ),
        migrations.CreateModel(
            name='Comment_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='имя автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='текст коментария')),
                ('FK_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Comment_Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий к ответу')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Answers')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Users')),
            ],
            options={
                'verbose_name': 'Комментарий к ответам',
                'verbose_name_plural': 'Комментарии к ответам',
            },
        ),
        migrations.AddField(
            model_name='answers',
            name='homework_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Homework'),
        ),
        migrations.AddField(
            model_name='answers',
            name='profs_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Profs'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Students'),
        ),
    ]
