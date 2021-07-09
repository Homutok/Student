from django import forms
from .models import Student, Comment
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class FilterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'faculty', 'status',)
        labels = {'student_name': 'ФИО', 'faculty': 'Факультет', 'status': 'Статус', }


class CommentForm(forms.ModelForm):
    """Добавление Комментария"""
    # def is_valid(self):
    #
    #     return 1

    class Meta:
        model = Comment
        fields = "__all__"


