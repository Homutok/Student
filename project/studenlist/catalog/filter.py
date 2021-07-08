import django_filters
from django_filters.filters import ChoiceFilter
from .models import Student

EMPTY_CHOICE = ('', '---------')


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        #mentor = django_filters.CharFilter(lookup_expr='icontains')
        fields = ['student_name', 'status']

    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)
        choices = filter(
            lambda f: isinstance(self.filters[f], ChoiceFilter),
            self.filters)

        for status in choices:
            extended_choices = ((EMPTY_CHOICE,) +
                                self.filters[status].extra['choices'])
            self.filters[status].extra['choices'] = extended_choices
