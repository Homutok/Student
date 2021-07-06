from django.shortcuts import render
from .models import Student, Profile, Comment, Department
from django.views import generic


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
    pass


class StudentDetailView(generic.DetailView):
    pass


# Просмотр списка университетов
class UniversityListView(generic.ListView):
    pass


class UniversityDetailView(generic.DetailView):
    pass


# Просмотр отделов
class DepartmentListView(generic.ListView):
    pass


class DepartmentDetailView(generic.DetailView):
    pass
