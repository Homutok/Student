from django.shortcuts import render
from .models import Student, Profile, Comment, Department,University
from django.views import generic
from django.http import Http404


# Create your views here.
def index(request):
    num_working_student = Student.objects.filter(status__exact='study').count()
    num_department = Department.objects.all().count()
    num_mentors = Profile.objects.filter(role_of_user__icontains='mentor').count()
    return render(request, 'index.html',
                  context={'num_working_student': num_working_student,
                           'num_department': num_department,
                           'num_mentors': num_mentors})


# Просмотр страницы с студентами
class StudentListView(generic.ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'catalog/student_list.html'


class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_data'] = Comment.objects.filter(comment=self.object)

        print(context)
        return context

    def guide_detail_view(request, pk):
        try:
            student_id = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404(" Записи не сщуествет ¯\_(ツ)_/¯ ")
        return render(
            request,
            'catalog/student_detail.html',
            context={'guide': student_id, }
        )


# Просмотр списка университетов
class UniversityListView(generic.ListView):
    model = University
    template_name = 'catalog/university_list.html'
    paginate_by = 10

    def get_queryset(self):
        return University.objects.order_by('name_of_university')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['borrowed'] = True
        return context

class UniversityDetailView(generic.DetailView):
    model = University
    template_name = 'catalog/university_detail.html'
    paginate_by = 10

    def get_queryset(self):
        return University.objects.order_by('name_of_university')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['borrowed'] = True
        return context


# Просмотр отделов
class DepartmentListView(generic.ListView):
    pass


class DepartmentDetailView(generic.DetailView):
    pass
