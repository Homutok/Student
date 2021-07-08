from django.urls import path, re_path
from django.views.decorators.http import require_POST

from .views import views_index, views_student, views_department, views_university


urlpatterns = [
    path('', views_index.index, name='index'),
    re_path(r'^$', views_index.index, name='index'),
]
urlpatterns += [
    re_path(r'^students/$', views_student.StudentListView.as_view(), name='student'),
    re_path(r'^students/$', views_student.filter_students, name='tets_filter'),
    re_path(r'^student/(?P<pk>\d+)$', views_student.StudentDetailView, name='student-detail'),
]
urlpatterns += [
    re_path(r'^student/create/$', views_student.StudentCreate.as_view(), name='student_create'),
    re_path(r'^student/(?P<pk>\d+)/update/$', views_student.StudentUpdate.as_view(), name='student_update'),
    re_path(r'^student/(?P<pk>\d+)/delete/$', views_student.StudentDelete.as_view(), name='student_delete'),
    re_path(r'^student/(?P<pk>\d+)/comment/$', views_student.CommentCreate.as_view(), name='comment_create'),
]
urlpatterns += [
    re_path(r'^universities/$', views_university.UniversityListView.as_view(), name='university'),
    re_path(r'^university/(?P<pk>\d+)$', views_university.UniversityDetailView.as_view(), name='university-detail'),
    re_path(r'^university/create/$', views_university.UniversityCreate.as_view(), name='university_create'),
    re_path(r'^university/(?P<pk>\d+)/update/$', views_university.UniversityUpdate.as_view(), name='university_update'),
    re_path(r'^university/(?P<pk>\d+)/delete/$', views_university.UniversityDelete.as_view(), name='university_delete'),
]
urlpatterns += [
    re_path(r'^signup/$', views_index.signup, name='signup'),

]
urlpatterns += [
    re_path(r'^departments/$', views_department.DepartmentListView.as_view(), name='department'),
    re_path(r'^department/(?P<pk>\d+)$', views_department.DepartmentDetailView.as_view(), name='department-detail'),
    re_path(r'^department/create/$', views_department.DepartmentCreate.as_view(), name='department_create'),
    re_path(r'^department/(?P<pk>\d+)/update/$', views_department.DepartmentUpdate.as_view(), name='department_update'),
    re_path(r'^department/(?P<pk>\d+)/delete/$', views_department.DepartmentDelete.as_view(), name='department_delete'),
]