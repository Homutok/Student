from ..models import Student, Comment
from ..forms import FilterStudentForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import Http404
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from ..filter import StudentFilter

# Просмотр страницы с студентами
class StudentListView(generic.ListView, generic.FormView):
    model = Student
    context_object_name = 'student_list'
    template_name = '../catalog/student_list.html'
    form_class = FilterStudentForm

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            query = ''
        student_list = Student.objects.filter(
            Q(student_name__icontains=query) | Q(status__icontains=query)
        )
        return student_list


class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_data'] = Comment.objects.filter(student=self.object)
        return context

    def guide_detail_view(request, pk):
        try:
            student_id = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404(" Записи не сщуествет ¯\_(ツ)_/¯ ")
        return render(
            request,
            '../catalog/student_detail.html',
            context={'guide': student_id, }
        )


class StudentCreate(CreateView):
    """Добавление Студента"""
    model = Student
    fields = '__all__'


class StudentUpdate(UpdateView):
    """Редактирование Студента"""
    model = Student
    fields = '__all__'


class StudentDelete(DeleteView):
    """Удаление Студента"""
    model = Student
    success_url = reverse_lazy('student')


class CommentCreate(CreateView):
    """Добавление Комментария"""
    model = Comment
    fields = '__all__'
    success_url = reverse_lazy('student')


class CommentDelete(DeleteView):
    """Добавление Комментария"""
    model = Comment
    success_url = reverse_lazy('student')


class CommentUpdate(UpdateView):
    """Добавление Комментария"""
    model = Comment
    fields = ['comment']
    success_url = reverse_lazy('student')


def product_list(request):
    f = StudentFilter(request.GET, queryset=Student.objects.all())
    return render(request,
                  'catalog/tests.html',
                  {'filter': f})

