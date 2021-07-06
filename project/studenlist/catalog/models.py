from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


#Модель студента
class Student(models.Model):
    student_name = models.CharField(max_length=100,db_index=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_study = models.CharField(max_length=200, db_index=True)
    faculty = models.CharField(max_length=200, db_index=True)

    STUDY = 'study'

    LOAN_STATUS = (
        (STUDY, 'Учится'),
        ('n', 'Отчислен'),
        ('w', 'Работает'),
        ('nw', 'Уволен'),
    )
    status = models.CharField(max_length=2, choices=LOAN_STATUS, blank=True, default='s', help_text='статус ученика')
    summary = models.CharField(max_length=1000, db_index=True)

    mentor_id = models.ForeignKey('Profile', on_delete=models.PROTECT, null=True)
    department_id = models.ForeignKey('Department', on_delete=models.PROTECT, null=True)

    begin_of_study = models.DateField(null=True, blank=True)


    @property
    def calculate_course(self):
        if self.begin_of_study:
            today = datetime.date.today()
            return today.year - self.begin_of_study.year - (
                        (today.month, today.day) < (self.begin_of_study.month, self.begin_of_study.day))
        return 0

    def __str__(self):
        return self.student_name


#Модель комментариев
class Comment(models.Model):
    comment = models.CharField(max_length=200, db_index=True)

    mentor_id = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.ForeignKey('Student', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.comment


#Расширение стандартного пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_of_user = models.CharField(max_length=100, db_index=True)

    department_id = models.ForeignKey('Department',on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.user.__str__()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


#Класс отдела
class Department(models.Model):
    department_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.department_name
