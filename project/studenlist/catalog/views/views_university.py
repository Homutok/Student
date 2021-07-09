from ..forms import UniversityForm
from ..models import University
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Просмотр списка университетов
class UniversityListView(generic.ListView):
    model = University
    template_name = '../catalog/university_list.html'
    paginate_by = 10

    def get_queryset(self):
        return University.objects.order_by('name_of_university')


class UniversityDetailView(generic.DetailView):
    model = University
    template_name = '../templates/catalog/university_detail.html'


class UniversityCreate(CreateView):
    model = University
    form_class = UniversityForm



class UniversityUpdate(UpdateView):
    model = University
    form_class = UniversityForm



class UniversityDelete(DeleteView):
    model = University
    success_url = reverse_lazy('departments')
