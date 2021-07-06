from django import forms

from .models import Student

class FilterStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('student_name', 'faculty','status',)