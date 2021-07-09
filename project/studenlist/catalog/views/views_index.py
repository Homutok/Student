from functools import wraps

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import Student, Profile, Department
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate



class indexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_working_student'] = Student.objects.filter(status__exact='study').count()
        context['num_department'] = Department.objects.all().count()
        context['num_mentors'] = Profile.objects.filter(role_of_user__icontains='mentor').count()
        return context


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