from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^students/$', views.StudentListView.as_view(), name='student'),
    re_path(r'^student/(?P<pk>\d+)$', views.StudentDetailView.as_view(), name='student-detail'),
]
urlpatterns += [
    re_path(r'^universities/$', views.UniversityListView.as_view(), name='university'),
    re_path(r'^university/(?P<pk>\d+)$', views.UniversityDetailView.as_view(), name='university-detail'),
    re_path(r'^departments/$', views.DepartmentListView.as_view(), name='department'),
]