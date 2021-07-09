import django_filters
from django_filters.filters import ChoiceFilter
from project.studenlist.catalog.models import Student

EMPTY_CHOICE = ('', '---------')

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
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
