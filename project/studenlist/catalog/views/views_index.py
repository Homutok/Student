from functools import wraps

from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..models import Student, Profile, Department
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate


def index(request):
    num_working_student = Student.objects.filter(status__exact='study').count()
    num_department = Department.objects.all().count()
    num_mentors = Profile.objects.filter(role_of_user__icontains='mentor').count()
    return render(request, 'index.html',
                  context={'num_working_student': num_working_student,
                           'num_department': num_department,
                           'num_mentors': num_mentors})



def do_not_need_to_login(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/catalog/')
    return wrap


@do_not_need_to_login
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            form.fields['username'].widget.attrs['placeholder'] = 'Введите никнейм'
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/catalog/')
    else:
        form = UserCreationForm()
        form.fields['username'].widget.attrs['placeholder'] = 'Введите никнейм'
    return render(request, 'signup.html', {'form': form})


class ProfilesUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'catalog/profile_form.html'

    def get_absolute_url(self):
        return redirect('/catalog/')