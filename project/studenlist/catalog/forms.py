from django import forms
from .models import Student, Comment,University,Department
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class FilterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'faculty', 'status',)
        labels = {'student_name': 'ФИО', 'faculty': 'Факультет', 'status': 'Статус', }


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = "__all__"
        labels = {'name_of_university': 'Университет', }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        labels = {'department_name': 'Отделение', 'summary': 'Описание' }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {'student_name': 'ФИО', 'student_photo': 'Фото','date_of_birth': 'Дата рождения', 'faculty': 'Факультет',
                  'status': 'Статус', 'summary': 'Описание','mentor': 'Наставник', 'department': 'Отделение','begin_of_study': 'Начало учебы',}


class CommentForm(forms.ModelForm):
    """Добавление Комментария"""

    class Meta:
        model = Comment
        fields = "__all__"
        success_url = reverse_lazy('student')

