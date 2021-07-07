from ..models import Department
from django.views import generic


class DepartmentListView(generic.ListView):
    model = Department
    template_name = '../catalog/department_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Department.objects.order_by('department_name')


class DepartmentDetailView(generic.DetailView):
    model = Department
    template_name = '../templates/catalog/department_detail.html'
