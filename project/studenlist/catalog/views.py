from django.shortcuts import render
from .models import Student, Profile,Comment,Department
# Create your views here.
def index(request):
    num_working_student = Student.objects.filter(status__exact='study').count()
    num_department = Department.objects.all().count()
    num_mentors = Profile.objects.filter(role_of_user__icontains='mentor').count()
    return render(request, 'index.html',
                  context={'num_working_student':num_working_student,
                           'num_department':num_department,
                           'num_mentors':num_mentors})