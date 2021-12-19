from django.db import models

# Create your models here.
from django.db import models

from django.db import models
from django.utils import timezone

SKILL_TYPES = (
    ('1', 'Начинающий'),
    ('2', 'Продлжающий'),
    ('3', 'профессионал'),
)


class User11(models.Model):
    login = models.CharField('Логин', max_length=30)
    password = models.CharField('Пароль', max_length=30)
    privilegies = models.BooleanField(default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        titel = self.login
        return titel


class Student(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    number = models.CharField('Номер телефона', max_length=11)
    date_of_birth = models.DateField('Дата рождения', default=timezone.now)
    skill_level = models.CharField('Уровень подготовки', max_length=1, choices=SKILL_TYPES)
    user_id = models.ForeignKey(User11, on_delete=models.CASCADE, db_column='Учетная запись')

    class Meta:
        verbose_name = 'Танцор'
        verbose_name_plural = 'Танцоры'
        ordering = ['surname']

    def __str__(self):
        titel = self.surname + ' ' + self.name + ' ' + self.middle_name
        return titel


class Style(models.Model):
    dance_style = models.CharField('Стиль танца', max_length=50)
    skill_level = models.CharField('Уровень подготовки', max_length=1, choices=SKILL_TYPES)

    class Meta:
        verbose_name = 'Группа по направлениям'
        verbose_name_plural = 'Группы по напарвлениям'

    def __str__(self):
        titel = self.dance_style + ' ' + self.skill_level
        return titel


class Manager(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    user_id = models.ForeignKey(User11, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def __str__(self):
        titel = self.surname + ' ' + self.name + ' ' + self.middle_name
        return titel


class Subscription(models.Model):
    number_of_lessons = models.CharField('Количество занятий', max_length=50)
    price = models.CharField('Цена', max_length=50)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Танцор')
    group_id = models.ForeignKey(Style, on_delete=models.CASCADE, verbose_name='Группа')
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name='Менеджер')

    class Meta:
        verbose_name = 'Абонимент'
        verbose_name_plural = 'Абонименты'

    def __str__(self):
        titel = str(self.student_id) + ". Количество занятий:" + self.number_of_lessons + '.  Группа:' + str(self.group_id)
        return titel


class Educator(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    number = models.CharField('Номер телефона', max_length=11)

    class Meta:
        verbose_name = 'Педагог'
        verbose_name_plural = 'Педагоги'

    def __str__(self):
        titel = self.surname + ' ' + self.name + ' ' + self.middle_name
        return titel


class Schedule(models.Model):
    date = models.DateField('Дата занятия', default=timezone.now)
    time = models.TimeField('Время занятия', default=timezone.now)
    group_id = models.ForeignKey(Style, on_delete=models.CASCADE, db_column='Группа')
    educator_id = models.ManyToManyField(Educator, db_column='Педагог')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self):
        titel = str(self.date) + ' ' + str(self.time) + ' ' + str(self.group_id)
        return titel


class Visit(models.Model):
    presence = models.BooleanField('Присутствие', default=0)
    subscription_id = models.ForeignKey(Subscription, on_delete=models.CASCADE, db_column='Абонемент')
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE, db_column='Занятие')
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='Танцор')

    def __str__(self):
        titel = str(self.student_id) + ' ' + str(self.schedule_id) + ' ' + str(self.presence)
        return titel

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
