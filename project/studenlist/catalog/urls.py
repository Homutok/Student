from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^students/$', views.StudentListView.as_view(), name='student'),
    re_path(r'^universities/$', views.UniversityListView.as_view(), name='university'),
    re_path(r'^departments/$', views.DepartmentListView.as_view(), name='department'),
]