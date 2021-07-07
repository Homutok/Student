from django.shortcuts import render


from .models import Student, Profile, Comment, Department,University
from django.views import generic
from django.http import Http404
from .forms import FilterStudentForm
from django.db.models import Q

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
class StudentListView(generic.ListView,generic.FormView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'catalog/student_list.html'
    form_class = FilterStudentForm

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        if query == None:
            query=''
        student_list = Student.objects.filter(
            Q(student_name__icontains = query) | Q(status__icontains = query)
        )
        return student_list

class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_data'] = Comment.objects.filter(comment=self.object)
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

class UniversityDetailView(generic.DetailView):
    model = University
    template_name = 'catalog/university_detail.html'
    paginate_by = 10


# Просмотр отделов
class DepartmentListView(generic.ListView):
    model = Department
    template_name = 'catalog/department_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Department.objects.order_by('department_name')


class DepartmentDetailView(generic.DetailView):
    model = Department
    template_name = 'catalog/department_detail.html'
    paginate_by = 10


def filter_students(request):
    if request.method == "POST":
        form = FilterStudentForm(request.POST)
        if form.is_valid():  # All validation rules pass
            student_name = form.cleaned_data['student_name']
            faculty = form.cleaned_data['faculty']
            status = form.cleaned_data['status']

            return render(request, 'catalog/student_list.html', {'form': form})
    else:
        form = FilterStudentForm()
    return render(request, 'catalog/student_list.html', {'form': form})