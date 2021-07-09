from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Department(models.Model):
    """Класс отдела"""
    department_name = models.CharField(max_length=100, db_index=True)
    summary = models.CharField(max_length=1000, db_index=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('department-detail', args=[str(self.id)])

    def __str__(self):
        return self.department_name
