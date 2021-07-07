from django import forms

from .models import Student,Faculty,Department


   # def save(self, commit=True):
      #  name = self.

      #  self.instance.student_name = name


class FilterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'faculty', 'status',)
        labels = {'student_name': 'ФИО', 'faculty': 'Факультет', 'status': 'Статус', }