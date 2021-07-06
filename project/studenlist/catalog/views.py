from django.shortcuts import render
from .models import Student, Profile,Comment,Department
# Create your views here.
def index(request):
    num_working_student = Student.objects.all().count()
    num_department = Department.objects.all().count()
    num_mentors = 1
    return render(request,'index.html',
                  context={'num_working_student':num_working_student,
                           'num_department':num_department,
                           'num_mentors':num_mentors})