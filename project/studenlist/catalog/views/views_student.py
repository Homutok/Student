from ..models import Student, Comment
from ..forms import FilterStudentForm,CommentForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
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


class StudentDetailView(generic.DetailView, generic.FormView):
    model = Student
    context_object_name = 'student'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # query = self.request.GET.get('comment')
        # if query is None:
        #     query="None"
        context['comment_data'] = Comment.objects.filter(student=self.object)
        # context['comment'] = query
        return context

    def form_valid(self, form):
        form.send_email()
        print(form)
        return super(StudentDetailView, self).form_valid(form)

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


# def StudentDetailView(request, year, month, day, student):
#     student = Student
#     comments = student.co comments.filter(active=True)
#     new_comment = None
#     if request.method == 'POST':
#         # Комментарий был опубликован
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Создайте объект Comment, но пока не сохраняйте в базу данных
#             new_comment = comment_form.save(commit=False)
#             # Назначить текущий пост комментарию
#             new_comment.post = post
#             # Сохранить комментарий в базе данных
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request,
#                   'blog/post/detail.html',
#                   {'post': post,
#                    'comments': comments,
#                    'new_comment': new_comment,
#                    'comment_form': comment_form})

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

