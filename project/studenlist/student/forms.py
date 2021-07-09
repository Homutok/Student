from django import forms
from .models import Student, Comment
from django.urls import reverse_lazy


class FilterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'faculty', 'status',)
        labels = {'student_name': 'ФИО', 'faculty': 'Факультет', 'status': 'Статус', }


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

