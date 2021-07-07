from django import forms

from .models import Student,Faculty

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('student_name','faculty','status',)
        labels = {'student_name':'ФИО','faculty':'Факультет','status':'Статус',}

class FacultyForm(forms.ModelForm):
    name = forms.CharField(label='name')
    class Meta:
        model = Faculty
        fields = ('faculty_name','university',)
        labels = {'faculty_name':'Факультет','university':'Учебное заведение',}

   # def save(self, commit=True):
      #  name = self.

      #  self.instance.student_name = name


class FilterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'faculty', 'status',)
        labels = {'student_name': 'ФИО', 'faculty': 'Факультет', 'status': 'Статус', }