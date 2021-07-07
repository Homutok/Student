from ..models import University
from django.views import generic


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
