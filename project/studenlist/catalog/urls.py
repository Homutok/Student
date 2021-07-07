from django.urls import path, re_path
from .views import views_index, views_student, views_department, views_university


urlpatterns = [
    path('', views_index.index, name='index'),
    re_path(r'^$', views_index.index, name='index'),
    re_path(r'^students/$', views_student.StudentListView.as_view(), name='student'),
    re_path(r'^students/$', views_student.filter_students, name='tets_filter'),
    re_path(r'^student/(?P<pk>\d+)$', views_student.StudentDetailView.as_view(), name='student-detail'),
]
urlpatterns += [
    re_path(r'^student/create/$', views_student.StudentCreate.as_view(), name='student_create'),
    re_path(r'^student/(?P<pk>\d+)/update/$', views_student.StudentUpdate.as_view(), name='student_update'),
    re_path(r'^student/(?P<pk>\d+)/delete/$', views_student.StudentDelete.as_view(), name='student_delete'),
]
urlpatterns += [
    re_path(r'^universities/$', views_university.UniversityListView.as_view(), name='university'),
    re_path(r'^university/(?P<pk>\d+)$', views_university.UniversityDetailView.as_view(), name='university-detail'),
]

urlpatterns += [
    re_path(r'^departments/$', views_department.DepartmentListView.as_view(), name='department'),
    re_path(r'^department/(?P<pk>\d+)$', views_department.DepartmentDetailView.as_view(), name='department-detail'),
]