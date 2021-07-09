from ..forms import DepartmentForm
from ..models import Department, Profile, Student
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class DepartmentListView(generic.ListView):
    model = Department
    template_name = '../catalog/department_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Department.objects.order_by('department_name')


class DepartmentDetailView(generic.DetailView):
    model = Department
    template_name = '../templates/catalog/department_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_data'] = Student.objects.filter(department=self.object)
        context['user_data'] = Profile.objects.filter(department=self.object)
        return context


class DepartmentCreate(CreateView):
    model = Department
    form_class = DepartmentForm


class DepartmentUpdate(UpdateView):
    model = Department
    form_class = DepartmentForm


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('departments')
