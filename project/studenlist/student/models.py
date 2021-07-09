from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db import models
import datetime


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100, db_index=True)
    student_photo = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100, null=True,
                                      blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.PROTECT, null=True, related_name='faculty_of_student')

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
    status = models.CharField(max_length=50, choices=LOAN_STATUS, blank=True, default='study', help_text='статус '
                                                                                                         'ученика')
    summary = models.CharField(max_length=1000, db_index=True, null=True)

    mentor = models.ForeignKey('Profile', on_delete=models.PROTECT, null=True, related_name='mentor_of_student')
    department = models.ForeignKey('Department', on_delete=models.PROTECT, null=True, related_name='department_of_job')

    begin_of_study = models.DateField(null=True, blank=True)

    @property
    def calculate_course(self):
        if self.begin_of_study:
            today = datetime.date.today()
            return 1 + today.year - self.begin_of_study.year - (
                    (today.month, today.day) < (self.begin_of_study.month, self.begin_of_study.day))
        return 0

    class Meta:
        ordering = ['student_name']

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])

    def __str__(self):
        return self.student_name


# Модель комментариев
class Comment(models.Model):
    comment = models.CharField(max_length=300, db_index=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey('Student', on_delete=models.PROTECT, null=True, related_name='comment_for_student')

    def __str__(self):
        return self.comment