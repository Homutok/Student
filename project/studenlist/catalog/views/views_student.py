import urllib

from ..models import Student, Comment,Profile, Faculty, Department
from ..forms import FilterStudentForm,CommentForm
from ..models import Student, Comment,Profile
from ..forms import FilterStudentForm, CommentForm, StudentForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, QueryDict
from django.db.models import Q
from django.urls import reverse_lazy, reverse
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

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     self.view = StudentDetailView.as_view

class StudentDetailView(generic.DetailView, generic.FormView):
    model = Student
    context_object_name = 'student'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        custom_data = {'comment': request.POST['comment'], 'mentor': str(request.user.id), 'student': self.object.id}
        query_str = urllib.parse.urlencode(custom_data, doseq=False)
        custom_query_dict = QueryDict(query_str)
        # form = self.get_form()
        comment_form = CommentForm(data=custom_query_dict)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            return self.form_valid(comment_form)
        else:
            return self.form_invalid(comment_form)

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        # self.view = StudentDetailView.as_view()
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
    form_class = StudentForm


class StudentUpdate(UpdateView):
    """Редактирование Студента"""
    model = Student
    form_class = StudentForm


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


def student_list(request):
    f = StudentFilter(request.GET, queryset=Student.objects.all())
    return render(request,
                  'catalog/students_list.html',
                  {'filter': f})


def my_student_list(request):
    query = request.user
    f = StudentFilter(request.GET, queryset=Student.objects.filter(mentor__user=query))
    return render(request,
                  'catalog/students_list.html',
                  {'filter': f})


def faculty_student_list(request, pk):
    query = get_object_or_404(Faculty, pk=pk)
    f = StudentFilter(request.GET, queryset=Student.objects.filter(faculty=query))
    return render(request,
                  'catalog/students_list.html',
                  {'filter': f})


def department_student_list(request, pk):
    query = get_object_or_404(Department, pk=pk)
    f = StudentFilter(request.GET, queryset=Student.objects.filter(department=query))
    return render(request,
                  'catalog/students_list.html',
                  {'filter': f})