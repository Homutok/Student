from django.db import models
from django.shortcuts import reverse


# Create your models here.
class University(models.Model):
    name_of_university = models.CharField(max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse('university-detail', args=[str(self.id)])

    def __str__(self):
        return self.name_of_university


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200, db_index=True)
    university = models.ForeignKey('University', related_name='faculty_of_university', on_delete=models.PROTECT,null=True,)

    def get_absolute_url(self):
        return reverse('student_faculty', args=[str(self.id)])

    def __str__(self):
        return '%s (%s)' % (self.faculty_name, self.university)