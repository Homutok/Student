from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


# Модель студента
class Student(models.Model):
    student_name = models.CharField(max_length=100, db_index=True)
    date_of_birth = models.DateField(null=True, blank=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.PROTECT, null=True)

    STUDY = 'study'
    DEDUCTED = 'deducted'
    WORK = 'work'
    FIRED = 'fired'
    LOAN_STATUS = (
        (STUDY, 'Учится'),
        (DEDUCTED, 'Отчислен'),
        (WORK, 'Работает'),
        (FIRED, 'Уволен'),
    )
    status = models.CharField(max_length=50, choices=LOAN_STATUS, blank=True, default='s', help_text='статус ученика')
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

    class Meta:
        ordering = ['student_name']

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

    def __str__(self):
        return self.student_name


class University(models.Model):
    name_of_university = models.CharField(max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse('university-detail', args=[str(self.id)])

    def __str__(self):
        return self.name_of_university



class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200, db_index=True)
    university_id = models.ForeignKey('University',related_name='faculty_of_university', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.faculty_name


# Модель комментариев
class Comment(models.Model):
    comment = models.CharField(max_length=300, db_index=True)

    mentor_id = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.ForeignKey('Student', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.comment


# Расширение стандартного пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_of_user = models.CharField(max_length=100, db_index=True)
    department_id = models.ForeignKey('Department', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.user.__str__()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Класс отдела
class Department(models.Model):
    department_name = models.CharField(max_length=100, db_index=True)


    def __str__(self):
        return self.department_name
